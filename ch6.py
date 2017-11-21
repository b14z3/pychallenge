import pickle
import requests

from shared import format_solution, mkdir

mkdir("ch6")

page_url = "http://www.pythonchallenge.com/pc/def/peak.html"

# The page source indicated tht you shold look into pickle and has a link to a banner.p file
banner_url = "http://www.pythonchallenge.com/pc/def/banner.p"
banner = requests.get(banner_url).content
pickle_file = "ch6/pickle"
with open(pickle_file, 'wb') as p:
    p.write(banner)

pickle_content = pickle.load(open("ch6/pickle", "rb"))

# This part was sort of non-intuitive but I guess the banner part was the best clue. The lines are in the form of a
# tuple within a list [(' ', 95)]. Basically we need to multipy the key by the value to print out the banner
for line in pickle_content:
    print("".join([k * v for k, v in line]))

banner_text = """
              #####                                                                      ##### 
               ####                                                                       #### 
               ####                                                                       #### 
               ####                                                                       #### 
               ####                                                                       #### 
               ####                                                                       #### 
               ####                                                                       #### 
               ####                                                                       #### 
      ###      ####   ###         ###       #####   ###    #####   ###          ###       #### 
   ###   ##    #### #######     ##  ###      #### #######   #### #######     ###  ###     #### 
  ###     ###  #####    ####   ###   ####    #####    ####  #####    ####   ###     ###   #### 
 ###           ####     ####   ###    ###    ####     ####  ####     ####  ###      ####  #### 
 ###           ####     ####          ###    ####     ####  ####     ####  ###       ###  #### 
####           ####     ####     ##   ###    ####     ####  ####     #### ####       ###  #### 
####           ####     ####   ##########    ####     ####  ####     #### ##############  #### 
####           ####     ####  ###    ####    ####     ####  ####     #### ####            #### 
####           ####     #### ####     ###    ####     ####  ####     #### ####            #### 
 ###           ####     #### ####     ###    ####     ####  ####     ####  ###            #### 
  ###      ##  ####     ####  ###    ####    ####     ####  ####     ####   ###      ##   #### 
   ###    ##   ####     ####   ###########   ####     ####  ####     ####    ###    ##    #### 
      ###     ######    #####    ##    #### ######    ###########    #####      ###      ######
"""

format_solution("channel")