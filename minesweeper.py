#made by Abeer Choubey, to use this program, first instal PyQt5 by running 'pip install PyQt5' without the (') in terminal or cmd for windows
import sys
import random
from functools import partial
from PyQt5.QtCore import Qt, QTimer, QPropertyAnimation, QEasingCurve, pyqtProperty
from PyQt5.QtGui import QPainter, QColor, QFont, QLinearGradient, QBrush
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QGridLayout, QLabel, QVBoxLayout, QHBoxLayout,
    QMainWindow, QAction, QSpinBox, QMessageBox, QFrame
)

class CellButton(QPushButton):
    def __init__(self, row, col, size=44):
        super().__init__()
        self.row = row
        self.col = col
        self.setCheckable(True)
        self._reveal_progress = 0.0
        self.setFixedSize(size, size)
        self.is_mine = False
        self.adjacent = 0
        self.is_flagged = False
        self.is_revealed = False
        self._hover = False

        self.anim = QPropertyAnimation(self, b"reveal_progress")
        self.anim.setDuration(240)
        self.anim.setEasingCurve(QEasingCurve.InOutCubic)

        self.setStyleSheet("border: none; background: transparent;")

    def paintEvent(self, event):
        p = QPainter(self)
        rect = self.rect()

        grad = QLinearGradient(0, 0, 0, rect.height())
        if self.is_revealed:
            grad.setColorAt(0, QColor(240, 240, 245))
            grad.setColorAt(1, QColor(220, 220, 235))
        else:
            base_top = QColor(70, 100, 170)
            base_bot = QColor(30, 60, 130)
            if self._hover:
                base_top = base_top.lighter(120)
                base_bot = base_bot.lighter(120)
            t = self._reveal_progress
            top = QColor(int(base_top.red() * (1 - t) + 230 * t),
                         int(base_top.green() * (1 - t) + 230 * t),
                         int(base_top.blue() * (1 - t) + 235 * t))
            bot = QColor(int(base_bot.red() * (1 - t) + 210 * t),
                         int(base_bot.green() * (1 - t) + 210 * t),
                         int(base_bot.blue() * (1 - t) + 235 * t))
            grad.setColorAt(0, top)
            grad.setColorAt(1, bot)

        p.setBrush(QBrush(grad))
        p.setPen(Qt.NoPen)
        p.drawRoundedRect(rect, 6, 6)

        if self._reveal_progress > 0.3 and self.is_revealed:
            inset = 6
            inner = rect.adjusted(inset, inset, -inset, -inset)
            p.setPen(Qt.NoPen)
            inner_grad = QLinearGradient(0, 0, 0, inner.height())
            inner_grad.setColorAt(0, QColor(255, 255, 255))
            inner_grad.setColorAt(1, QColor(230, 230, 240))
            p.setBrush(QBrush(inner_grad))
            p.drawRoundedRect(inner, 5, 5)
            if self.is_mine:
                r = inner.center()
                rad = min(inner.width(), inner.height()) // 5
                p.setBrush(QBrush(QColor(40, 40, 40)))
                p.drawEllipse(r, rad, rad)
            elif self.adjacent > 0:
                font = QFont("Segoe UI", max(10, inner.height() // 2), QFont.Bold)
                p.setFont(font)
                colors = {
                    1: QColor(30, 110, 220),
                    2: QColor(30, 160, 60),
                    3: QColor(220, 60, 60),
                    4: QColor(100, 40, 200),
                    5: QColor(160, 60, 60),
                    6: QColor(20, 140, 140),
                    7: QColor(50, 50, 50),
                    8: QColor(120, 120, 120),
                }
                p.setPen(colors.get(self.adjacent, QColor(40, 40, 40)))
                p.drawText(inner, Qt.AlignCenter, str(self.adjacent))
        elif self.is_flagged:
            p.setBrush(QBrush(QColor(220, 40, 60)))
            p.drawRect(rect.width()//4, rect.height()//4, rect.width()//2, rect.height()//2)

    def enterEvent(self, event):
        self._hover = True
        self.update()

    def leaveEvent(self, event):
        self._hover = False
        self.update()

    def start_reveal_anim(self):
        if self.is_revealed:
            return
        self.is_revealed = True
        self.anim.stop()
        self.anim.setStartValue(self._reveal_progress)
        self.anim.setEndValue(1.0)
        self.anim.start()

    def set_flag(self, v: bool):
        self.is_flagged = v
        self.update()

    def reset(self):
        self.is_mine = False
        self.adjacent = 0
        self.is_flagged = False
        self.is_revealed = False
        self._reveal_progress = 0.0
        self.update()

    def get_reveal_progress(self):
        return self._reveal_progress

    def set_reveal_progress(self, val):
        self._reveal_progress = val
        self.update()

    reveal_progress = pyqtProperty(float, get_reveal_progress, set_reveal_progress)

class MinesweeperBoard(QWidget):
    def __init__(self, main_window, rows=9, cols=9, mines=10):
        super().__init__()
        self.main_window = main_window
        self.rows = rows
        self.cols = cols
        self.mines = mines

        self.grid = QGridLayout()
        self.grid.setSpacing(8)
        self.grid.setContentsMargins(10, 10, 10, 10)
        self.setLayout(self.grid)

        self.cells = [[None for _ in range(cols)] for __ in range(rows)]
        self._build_board()

        self.first_click = True
        self.timer = QTimer()
        self.timer.timeout.connect(self._tick)
        self.elapsed = 0
        self.flags_left = mines

    def _build_board(self):
        size = max(36, min(64, int(540 / max(self.rows, self.cols))))
        for r in range(self.rows):
            for c in range(self.cols):
                btn = CellButton(r, c, size=size)
                btn.clicked.connect(partial(self.left_click, r, c))
                btn.setContextMenuPolicy(Qt.CustomContextMenu)
                btn.customContextMenuRequested.connect(lambda _, rr=r, cc=c: self.right_click(rr, cc))
                self.grid.addWidget(btn, r, c)
                self.cells[r][c] = btn

    def place_mines(self, safe_r, safe_c):
        coords = [(r, c) for r in range(self.rows) for c in range(self.cols) if not (r == safe_r and c == safe_c)]
        mines_coords = random.sample(coords, self.mines)
        for (r, c) in mines_coords:
            self.cells[r][c].is_mine = True
        for r in range(self.rows):
            for c in range(self.cols):
                if not self.cells[r][c].is_mine:
                    self.cells[r][c].adjacent = self._count_adj(r, c)

    def _count_adj(self, r, c):
        cnt = 0
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                rr, cc = r + dr, c + dc
                if 0 <= rr < self.rows and 0 <= cc < self.cols:
                    if self.cells[rr][cc].is_mine:
                        cnt += 1
        return cnt

    def left_click(self, r, c):
        btn = self.cells[r][c]
        if btn.is_flagged or btn.is_revealed:
            return
        if self.first_click:
            self.place_mines(r, c)
            self.first_click = False
            self.elapsed = 0
            self.timer.start(1000)
        if btn.is_mine:
            self._reveal_all_mines()
            self.timer.stop()
            QMessageBox.information(self, "Boom!", "You clicked a mine. Game over.")
            return
        self._reveal_recursive(r, c)
        if self._check_win():
            self.timer.stop()
            self._reveal_all_safe()
            QMessageBox.information(self, "GG!", f"You cleared the board in {self.elapsed} seconds!")

    def right_click(self, r, c):
        btn = self.cells[r][c]
        if btn.is_revealed:
            return
        btn.set_flag(not btn.is_flagged)
        if btn.is_flagged:
            self.flags_left -= 1
        else:
            self.flags_left += 1
        self.main_window.update_status()

    def _reveal_recursive(self, r, c):
        stack = [(r, c)]
        seen = set()
        while stack:
            rr, cc = stack.pop()
            if (rr, cc) in seen:
                continue
            seen.add((rr, cc))
            btn = self.cells[rr][cc]
            if btn.is_flagged or btn.is_revealed:
                continue
            btn.start_reveal_anim()
            if btn.adjacent == 0 and not btn.is_mine:
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        if dr == 0 and dc == 0:
                            continue
                        rrr, ccc = rr + dr, cc + dc
                        if 0 <= rrr < self.rows and 0 <= ccc < self.cols:
                            stack.append((rrr, ccc))

    def _reveal_all_mines(self):
        for row in self.cells:
            for btn in row:
                if btn.is_mine:
                    btn.start_reveal_anim()

    def _reveal_all_safe(self):
        for row in self.cells:
            for btn in row:
                if not btn.is_mine:
                    btn.start_reveal_anim()

    def _check_win(self):
        return all(btn.is_mine or btn.is_revealed for row in self.cells for btn in row)

    def reset(self):
        self.first_click = True
        self.timer.stop()
        self.elapsed = 0
        self.flags_left = self.mines
        for row in self.cells:
            for btn in row:
                btn.reset()

    def _tick(self):
        self.elapsed += 1
        self.main_window.update_status()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Minesweeper")

        self.central = QFrame()
        self.setCentralWidget(self.central)
        self.vlay = QVBoxLayout(self.central)

        top = QHBoxLayout()
        self.flag_label = QLabel()
        self.time_label = QLabel()
        self.reset_btn = QPushButton("Restart")
        self.reset_btn.clicked.connect(self.on_reset)
        top.addWidget(self.flag_label)
        top.addWidget(self.reset_btn)
        top.addWidget(self.time_label)
        self.vlay.addLayout(top)

        self.board = MinesweeperBoard(self, 9, 9, 10)
        self.vlay.addWidget(self.board)

        bottom = QHBoxLayout()
        self.rows_spin = QSpinBox()
        self.rows_spin.setRange(6, 24)
        self.rows_spin.setValue(9)
        self.cols_spin = QSpinBox()
        self.cols_spin.setRange(6, 30)
        self.cols_spin.setValue(9)
        self.mines_spin = QSpinBox()
        self.mines_spin.setRange(1, 200)
        self.mines_spin.setValue(10)
        new_btn = QPushButton("New Game")
        new_btn.clicked.connect(self.new_game)
        bottom.addWidget(self.rows_spin)
        bottom.addWidget(self.cols_spin)
        bottom.addWidget(self.mines_spin)
        bottom.addWidget(new_btn)
        self.vlay.addLayout(bottom)

        self.update_status()

    def on_reset(self):
        self.board.reset()
        self.update_status()

    def new_game(self):
        r, c, m = self.rows_spin.value(), self.cols_spin.value(), self.mines_spin.value()
        self.vlay.removeWidget(self.board)
        self.board.deleteLater()
        self.board = MinesweeperBoard(self, r, c, m)
        self.vlay.insertWidget(1, self.board)
        self.update_status()

    def update_status(self):
        self.flag_label.setText(f"Flags: {self.board.flags_left}")
        self.time_label.setText(f"Time: {self.board.elapsed}s")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
