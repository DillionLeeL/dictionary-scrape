import requests
from bs4 import BeautifulSoup
import string

f = open("crosswordwords.txt", "w")


URL = "https://www.xwordinfo.com/Popular"
page=requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

lines = soup.find("table", id="CPHContent_XTable")

for line in lines:
    output = (line.text.strip()).translate({ord(ch): None for ch in '0123456789.'}).split()
    for word in output:
        print(word.lower())
        f.write(word.lower())
        f.write("\n")

f.close()