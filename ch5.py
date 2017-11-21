import requests
import re

from shared import format_solution

page_url = "http://www.pythonchallenge.com/pc/def/linkedlist.html"


# Solved it with recursive scraper
def get_id(id):
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}".format(id)
    r = requests.get(url)
    text = r.text
    if "Divide by two" in text:
        # About halfway through the message is to divide the id in half so that's what we do here
        next_id = str(int(id) / 2)
    elif "next nothing" in text:
        # If there is another id to scrape pull it and extract the id
        next_id = re.findall(r'[0-9]{1,10}$', text)[0]
    else:
        # This is the base case and signals that we're done scraping and we've found the end of the line
        return r.text.replace(".html", "")
    # If we haven't returned from the base case then we call the function again via return. This is recursive and
    # continues scraping until it hits the base case and returns without calling itself again.
    return get_id(next_id)


print("Starting scraping. This will take a minute...")
format_solution(get_id("12345"))
