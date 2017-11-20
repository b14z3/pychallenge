import requests
import zipfile
import re

from solved import format_solution

# Get the file
url = "http://www.pythonchallenge.com/pc/def/channel.zip"

# Save it to disk
r = requests.get(url)
outfile = "ch7/channel.zip"
with open(outfile, "wb") as f:
    f.write(r.content)

# Create a zipfile object
file = zipfile.ZipFile(outfile)

# The final text says check the comments. Zip files have comments apparently so build a list to store them as they're
# iterated through
comments = []


# Solved it with a recursive function to iterate through all of the files, getting the next id,
# and getting the comments along the way
def get_id(zipf, id):
    file = "{}.txt".format(id)
    # Add the comment for the given file to the list
    comments.append(zipf.getinfo(file).comment.decode("utf-8"))
    text = zipf.read(file).decode("utf-8")
    if "Divide by two" in text:
        next_id = str(int(id) / 2)
    elif "Next nothing" in text:
        next_id = re.findall(r'[0-9]{1,10}$', text)[0]
    else:

        print(id, text)
        return text
    return get_id(zipf, next_id)

# Follow the clues and build the comment list
get_id(file, "90052")

# Print out the ASCII art which is "hockey"
print("".join(comments))

print("Going to the link below says 'it's in the air. look at the letters.'")
format_solution("hockey")

print("HOCKEY is spelled out with the letters O X Y G E N... oxygen")
format_solution("oxygen")
