# dictionary-scrape
Web scrapper for dictionary.com to pull all words a-z

This webscrapper works as of Nov 2021, but may not work in the future if the HTML of dictionary.com changes.

*****************
Note: dictionary.com has several issues in the way their words are cataloged:
- some entries are listed non-alphabetically
- duplicate entries
- different versions of words are sometimes listed as the same word (i.e. "quicker" and "quickness" both being listed as "quick"), meaning this dictionary is non-complete

Further processing of the output file to remove duplicates and alphabetize entries is recommended.
*****************

Arguments:

--alpha     Remove entries that contain hyphens, spaces, numbers, or other non-letter characters
--full      Allow only full words, removing acronyms and initialisms

Recommended usage: python ./dictionaryscrape.py --alpha --full
