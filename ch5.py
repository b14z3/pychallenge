import requests
import re

from solved import format_solution


# Solved it with recursive scraper
def get_id(id):
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}".format(id)
    r = requests.get(url)
    text = r.text
    if "Divide by two" in text:
        next_id = str(int(id) / 2)
    elif "next nothing" in text:
        next_id = re.findall(r'[0-9]{1,10}$', text)[0]
    else:
        return r.text.replace(".html", "")
    return get_id(next_id)


print("Starting scraping...")
format_solution(get_id("12345"))
