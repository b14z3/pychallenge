import requests
from PIL import Image

from shared import format_solution, mkdir

mkdir("ch11")

page_url = "http://www.pythonchallenge.com/pc/return/5808.html"

# The page title is odd-even and the picture looks a bit blurred. Guessing that there are two images here or some
# steganography going on. Let's look at every other pixel

img_url = "http://www.pythonchallenge.com/pc/return/cave.jpg"
img_file = "ch11/cave.jpg"

# This request was it kept throwing 401's and I noticed the response header was:
# 'WWW-Authenticate': 'Basic realm="inflate"'
# I passed in the creds from the previous inflate challenge and boom, it worked
# r = requests.get(img_url, auth=("huge", "file"))
# if r.status_code == 200:
#     with open(img_file, 'wb') as i:
#         i.write(r.content)
# else:
#     print("Need some kind of auth and the response headers say WWW-Authenticate': 'Basic realm='inflate'")

img = Image.open(img_file)
width = img.width
height = img.height

# Create an even and an odd image which we'll populate. Size will be half since each image will be comprised of half
# the pixels of the parent image. (use floor division)
even = Image.new('RGB', (width // 2, height // 2))
odd = Image.new('RGB', (width // 2, height // 2))

for w in range(0, width):
    for h in range(0, height):
        pixel = img.getpixel((w, h))
        pixel_content = (w // 2, h // 2)
        # Use modulus to see if it's an odd or even pixel
        if (w + h) % 2 == 0:
            even.putpixel(pixel_content, pixel)
        else:
            odd.putpixel(pixel_content, pixel)

even.save("ch11/even.jpg")
odd.save("ch11/odd.jpg")

# Oohhhhh spooky! The even picture contains one eerie word
even.show()

format_solution("evil", uri="return")