import os


def format_solution(solution, uri="def"):
    print("Solution:", "http://www.pythonchallenge.com/pc/{uri}/{solution}.html".format(uri=uri, solution=solution))


def mkdir(ch):
    if not os.path.isdir(ch):
        os.mkdir(ch)