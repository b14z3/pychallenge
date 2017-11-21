import requests
from PIL import Image

from shared import format_solution, mkdir

mkdir("ch12")

# evil.html is a picture named evil1.jpg. It's pixelated but not much there to manipulate. It just shows someone
# dealing 5 piles of cards and it looks like 5 on the piles. So 5 plays into it somehow. Turns out that there are other
# file named evil2.jpg, evil3.jpg, and evil4.jpg (not actually an image) which isn't a jpg at all. Evil2 seems most
# promising and says to look for a gfx file which happens to exist and looks promising (also protected by basic auth
# from inflate challenge)

img2_url = "http://www.pythonchallenge.com/pc/return/evil2.gfx"
img2_file = "ch12/evil2.gfx"

r = requests.get(img2_url, auth=("huge", "file"))
if r.status_code == 200:
    with open(img2_file, 'wb') as i:
        i.write(r.content)
else:
    print("need auth!")


# Let's get the raw data then split it into 5 images using every 5th pixel and see what we get
with open(img2_file, 'rb') as i:
    pixels = i.read()

# Looking at the headers in the debugger as they get split up show they are different file formats as outlines below
file_info = {
    "1": {"ext": "jpg", "bytes": pixels[0::5]},
    "2": {"ext": "png", "bytes": pixels[1::5]},
    "3": {"ext": "gif", "bytes": pixels[2::5]},
    "4": {"ext": "png", "bytes": pixels[3::5]},
    "5": {"ext": "jpg", "bytes": pixels[4::5]}
}

for f in file_info:
    with open("ch12/split_evil{}.{}".format(f, file_info[f]["ext"]), 'wb') as fh:
        fh.write(file_info[f]["bytes"])

# For some reason it looks like the 4th file (the png) is getting truncated and it does not contain IEND and ends up
# being corrupted. However, file one says "dis", two says "pro", 3 says "port", and five says "ity" but it's stuck out.
# This means that the options for the solution are likely either "disproportionate" or "disproportional".
# Checking both turns out that its disproportional
format_solution("disproportional", uri="return")

# This is sort of a lame win but I'll take it...
