import requests
from PIL import Image

from solved import format_solution

img = "http://www.pythonchallenge.com/pc/def/oxygen.png"
img_file = "ch8/oxygen.png"
r = requests.get(img)

with open(img_file, 'wb') as i:
    i.write(r.content)




