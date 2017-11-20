from solved import format_solution

cipher = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr " \
         "ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

ignore_chars = ["'", ".", "(", ")", " "]


def shift(ltr, num=2):
    abc = "abcdefghijklmnopqrstuvwxyz"
    index = abc.index(ltr) + num
    if index + 1 > len(abc):
        index = index - len(abc)
    return abc[index]


for letter in cipher:
    if letter in ignore_chars:
        print(letter, end="")
    else:
        print(shift(letter), end="")

# translation:
# i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's
# why this text is so long. using string.maketrans() is recommended. now apply on the url.

# maketrans is deprecated but we'll use our ceasar shift on the url: http://www.pythonchallenge.com/pc/def/map.html
print("\nURL is:")
solution = ""
for letter in "map":
    solution += shift(letter)

print("http://www.pythonchallenge.com/pc/def/{}.html".format(solution))
