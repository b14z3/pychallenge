from shared import format_solution

page_url = "http://www.pythonchallenge.com/pc/def/map.html"

cipher = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr " \
         "ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

ignore_chars = ["'", ".", "(", ")", " "]


# Judging from the image it looks like everything is shifted by 2 places. This is just a basic caesar cipher so let's
# build a function to do it for us for any given string.
def caesar_shift(ltr, num=2):
    abc = "abcdefghijklmnopqrstuvwxyz"
    index = abc.index(ltr) + num
    # Need to check if we have to "wrap around" to the beginning of the alphabet
    if index + 1 > len(abc):
        index = index - len(abc)
    return abc[index]


# Now lets iterate through the cipher text and shift as needed. We want to ignore symbols and spaces and just print
# them out without modification.
for letter in cipher:
    if letter in ignore_chars:
        print(letter, end="")
    else:
        print(caesar_shift(letter), end="")

# translation:
# i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's
# why this text is so long. using string.maketrans() is recommended. now apply on the url.

# maketrans is deprecated but we'll use our caesar_shift on the url now: http://www.pythonchallenge.com/pc/def/map.html
print("\n\nSolution is: ", end='')
solution = ""
for letter in "map":
    solution += caesar_shift(letter)

format_solution(solution)
