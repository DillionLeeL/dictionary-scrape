import json
from json import encoder
import requests
import html
from datetime import timedelta, date

# generator function for dates
def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

def main():
    url = "https://www.xwordinfo.com/JSON/Data.aspx"
    f = open("xwords.txt", "w")

    # For whatever reason the API will not return data on a GET without the "Referer" header
    my_headers = {
    "Accept": "application/json",
    "Accept-Encoding": "utf-8",
    "Connection": "keep-alive",
    "Referer": "https://www.xwordinfo.com/JSON/",
    "Host": "www.xwordinfo.com"
    }

    start_dt = date(2015, 12, 20)
    end_dt = date(2016, 1, 11)
    for dt in daterange(start_dt, end_dt):
        curr_dt = dt.strftime("%m/%d/%Y")

        try:
            res = requests.get(url, headers=my_headers, params="date="+curr_dt)
            res.encoding='utf-8'
            data=res.json(encoding='utf-8')

            for x in range(len(data["answers"]["across"])):
                # the api returns escaped character and numbers before the answers so split on that and take second element
                f.write(html.unescape(data["answers"]["across"][x])+'\n'+html.unescape(data["clues"]["across"][x]).split(". ")[1]+'\n')

        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

if __name__ == "__main__":
    main()