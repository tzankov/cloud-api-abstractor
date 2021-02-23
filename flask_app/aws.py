import sys
import inspect

def create():
    print("create")


def peer():
    print("peer")


function_list = [o[0] for o in inspect.getmembers(sys.modules[__name__], inspect.isfunction)]

actions = {}
for func in function_list:
    actions[func] = str(func +"()")