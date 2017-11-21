import re
import zipfile
import requests

from shared import format_solution, mkdir

mkdir("ch7")

page_url = "http://www.pythonchallenge.com/pc/def/channel.html"

# There is a comment in the page that indicates to look for a zip. Swap .zip for .html and get the zip file
url = "http://www.pythonchallenge.com/pc/def/channel.zip"

# Save it to disk
r = requests.get(url)
outfile = "ch7/channel.zip"
with open(outfile, "wb") as f:
    f.write(r.content)

# Create a zipfile object
file = zipfile.ZipFile(outfile)

# After starting at the file the readme suggests and iterating through the files the final text says check the comments.
# Zip files have comments apparently so build a list to store them as they're iterated through
comments = []


# Solved it with a recursive function to iterate through all of the files, getting the next id, and getting the comments
# along the way
def get_id(zipf, id_num):
    file_id = "{}.txt".format(id_num)
    # Add the comment for the given file to the list
    comments.append(zipf.getinfo(file_id).comment.decode("utf-8"))
    text = zipf.read(file_id).decode("utf-8")
    if "Divide by two" in text:
        next_id = str(int(id_num) / 2)
    elif "Next nothing" in text:
        next_id = re.findall(r'[0-9]{1,10}$', text)[0]
    else:
        # Base case to break out of the recursive loop
        return text
    return get_id(zipf, next_id)


# Follow the clues and build the comment list starting at the file number mentioned in the readme
get_id(file, "90052")

# Print out the ASCII art which is "hockey"
print("".join(comments))

print("Going to the link below says 'it's in the air. look at the letters.'")
format_solution("hockey")

print("HOCKEY is spelled out with the letters O X Y G E N... oxygen")
format_solution("oxygen")
