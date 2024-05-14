print("Downloading Cloud-Scraper...")
print("Setting Up!")
print("Performing Check...")
import time
import cloudscraper
from bs4 import BeautifulSoup
from urllib.parse import urlparse
print("Everything Looks Good! Lets Continue.")

url = "" #@param {type:"string"} 
print("Entered Link:")
print(url)
print("Checking Link...")
print("Checking Done!")
print("Bypassing Link...")
# ==============================================

def gplinks(url: str):
    client = cloudscraper.create_scraper(allow_brotli=False)
    p = urlparse(url)
    final_url = f"{p.scheme}://{p.netloc}/links/go"
    res = client.head(url)
    header_loc = res.headers["location"]
    p = urlparse(header_loc)
    ref_url = f"{p.scheme}://{p.netloc}/"
    h = {"referer": ref_url}
    res = client.get(url, headers=h, allow_redirects=False)
    bs4 = BeautifulSoup(res.content, "html.parser")
    inputs = bs4.find_all("input")
    time.sleep(10) # !important
    data = { input.get("name"): input.get("value") for input in inputs }
    h = {
        "content-type": "application/x-www-form-urlencoded",
        "x-requested-with": "XMLHttpRequest"
    }
    time.sleep(10)
    res = client.post(final_url, headers=h, data=data)
    try:
        return res.json()["url"].replace("/","/")
    except: 
        return "Could not Bypass your URL :("

# ==============================================

res = gplinks(url)

print(res)
print("Successfully Bypassed!")