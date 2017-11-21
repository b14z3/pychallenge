import re
import requests
from PIL import Image

from shared import format_solution, mkdir

mkdir("ch8")

page_url = "http://www.pythonchallenge.com/pc/def/oxygen.html"

# This image had a bar of gray pixels which looks interesting. Get the file and save it locally for inspection
img_url = "http://www.pythonchallenge.com/pc/def/oxygen.png"
img_file = "ch8/oxygen.png"
r = requests.get(img_url)

with open(img_file, 'wb') as i:
    i.write(r.content)

# There is a gray scale line directly in the center of the image so lets get that row and process it
img = Image.open(img_file)
center_row = img.height / 2

# get the pixel r/g/b/a for the center row from left to right
row = [img.getpixel((x, center_row)) for x in range(img.width)]

# looks like the boxes are 7 pixes wide so we'll use index stepping to just get one r/g/b/a from each pixel
row = row[::7]

# The last 3 pixels seem to be random values so we'll dump those
row = row[:-3]


# RGB colors have 255 possible values, just like ASCII... so maybe this is coded?
# Let's build a helper function for char conversion that takes in a list and returns a string
def convert_rgb_to_char(char_list):
    result = ""
    for char in char_list:
        result += chr(int(char))
    return result


# R/G/B are all equal in gray scale so we'll just use red to get a clean list
chars = [r for r, g, b, a in row]
msg = convert_rgb_to_char(chars)

# The initial hidden message
print("Initial hidden message in the gray pixels:\n", msg)

# Lets grab the list out of the hidden message and see what that decodes to
second_msg = re.search(r'\[(.*)\]', msg).group().replace("[", "").replace("]", "").replace(",", "")
second_msg = [x.strip() for x in second_msg.split()]

final_msg = convert_rgb_to_char(second_msg)

print("\nFinal message:", final_msg, "\n")

format_solution(final_msg)
