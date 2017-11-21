
from shared import format_solution

page_url = "http://www.pythonchallenge.com/pc/return/bull.html"

# In the source of the page there is a reference to sequence.txt which contains the following see and say sequence:
# a = [1, 11, 21, 1211, 111221,
# The goal is to find: len(a[30]) = ?


# The sequence is a "see and say".. one, one one, two ones, one two one one, etc etc.. so let's put it into a function
def see_and_say(number):
    result = ""
    # start out with the first number as the seed
    seed = number[0]
    # Set the remainder to the rest of the number. The + " " is a trick that plays with how python does indexing and
    # comparison. It's the "magic" in this function
    remainder = number[1:] + " "
    times = 1

    for num in remainder:
        if num != seed:
            result += str(times) + seed
            times = 1
            seed = num
        else:
            times += 1
    return result


# Seed the sequent list with the first number then get the last number in the list for each iteration
sequence = ["1"]
for x in range(0, 30):
    sequence.append(see_and_say(sequence[-1]))

solution = len(sequence[30])
format_solution(solution, uri="return")




