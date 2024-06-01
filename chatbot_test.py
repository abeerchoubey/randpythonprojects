import time
now=time.ctime()
qna = {
    "hi": "hey",
    "how are you?": "fine wbu",
    "what is your name": "My name is Atharv",
    "how old are you": "I am 14 years old",
    'what is time now':now,
    'who are you':'I am a CS student stuck in a computer talking to you',
    'i am good too':'nice',
}
print("Hello, type quit to exit this program.")
while True:
    q = input('You:')
    qs=q.lower()
    if qs == 'quit' or qs=="exit":
        break
    elif qs in qna:
        print(qna[qs])
    else:
        print('Sorry, I could not understand, Please try to rephrase.')
#I just modified your code a little bit
