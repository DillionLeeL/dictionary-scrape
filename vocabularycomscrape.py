import requests
from bs4 import BeautifulSoup
import string

f = open("vocab.txt", "w")


URL = "https://www.vocabulary.com/lists/1770071"
page=requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

lines = soup.find("ol", class_="wordlist")

for line in lines:
    output = line.text.strip()
    if output and output.find("and")==-1:
        print(output)
        f.write(output)
        f.write("\n")

f.close()