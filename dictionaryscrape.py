import types
import requests
from bs4 import BeautifulSoup
import string
import argparse

def main(args):
    alpha_only = args.alpha
    full_only = args.full

    f = open("words2.txt", "w", encoding="utf-8")

    for x in range(16,19):
        print("Scraping words that begin with", string.ascii_lowercase[x])
        # Maximum of 100 pages per letter
        for y in range(1,101):
            URL = "https://www.dictionary.com/list/"+ string.ascii_lowercase[x] + "/" + str(y)

            page=requests.get(URL)
            soup = BeautifulSoup(page.content, "html.parser")
            # returns NoneType on 404
            lines = soup.find("ul", class_="css-dy629s e12ye68r0")

            if lines is not None:
                for line in lines:
                    # Dictionary.com sometimes returns " | WORD synonyms", so this strips that
                    output = next(line.children).text.strip()
                    if output:
                        if alpha_only and not output.isalpha():
                            pass
                        elif full_only and output.isupper():
                            pass
                        else:
                            #print(output)
                            f.write(output)
                            f.write("\n")
            else:
                break

    f.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--alpha', action='store_true', help="Remove entries that contain hyphens, spaces, numbers, or other non-letter characters")
    parser.add_argument('--full', action='store_true', help="Allow only full words, removing acronyms and initialisms")
    args = parser.parse_args()
    main(args)