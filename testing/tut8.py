import random

"""
Note that code is required only for Q1b.
You may write your answers for Q1a and Q1c as comments.

The following code is already included for you:



"""

"""Your Answer Here"""

"""
a) a widget behaves like a man in a box but you cant see him, all you can do is give him items and instructions. 
E.g you can tell him to insert an object, he will take it and store it internally in one of 2 chests
the chest which he decides to put it in alternates every time you tell him to do so.
this alternation affects retrieve as well so if you insert and he puts it in chest 1, asking him to retrieve will then get contents from chest 2,
but using retrieve will not affect the item to be retrieved next.
Finally, asking him for stuff will make him give you both chests so you can see whats inside.
"""


def make_widget():
    stuff = ["empty", "empty", 0]

    def oplookup(msg, *args):
        if msg == "insert":
            place = stuff[2]
            stuff[place] = args[0]
            stuff[2] = (place + 1) % 2
        elif msg == "retrieve":
            return stuff[stuff[2]]
        elif msg == "stuff":
            return stuff
        else:
            raise Exception("widget doesn’t " + msg)

    return oplookup


widget = make_widget()
widget("insert", 1)
print(widget("stuff"))
widget("insert", 2)
print(widget("stuff"))
widget("insert", 3)
print(widget("stuff"))
print(widget("retrieve"))
print(widget("retrieve"))
print(widget("retrieve"))

"""
c) calling retrive 3 times will just yield "2" each time
"""


def make_accumulator():
    store = [0]

    def helper(num):
        store[0] += num
        return store[0]

    return helper
    pass


### DO NOT MODIFY THIS ###
A = make_accumulator()
B = make_accumulator()

print(A(10))
print(A(-90))
print(B(5))
print(B(89))


def make_monitored(f):
    count = [0]
    ### FILL YOUR CODE HERE ###
    def helper(x):
        if x == "how-many-calls?":
            return count[0]
        elif x == "reset-count":
            count[0] = 0
            pass
        else:
            count[0] += 1
            return f(x)

    return helper
    pass


### DO NOT MODIFY THIS ###
def double(x):
    return 2 * x


d = make_monitored(double)
print(d(1))
print(d(1))
print(d(1))
print()
print(d("how-many-calls?"))
print(d("reset-count"))
print(d("how-many-calls?"))


def make_monitored_extended(f):
    count = [0]
    ### FILL YOUR CODE HERE ###
    def helper(*x):
        if len(x) == 0:
            count[0] += 1
            return f()
        elif x[0] == "how-many-calls?":
            return count[0]
        elif x[0] == "reset-count":
            count[0] = 0
            pass

        else:
            count[0] += 1
            print(type(x))
            print(x)

            return f(*x)

    return helper
    pass
    # Leave your answers here #


### DO NOT MODIFY THIS ###
def sum_numbers(*numbers):
    s = 0
    for n in numbers:
        s = s + n
    return s


monitored_sum_numbers = make_monitored_extended(sum_numbers)
print(monitored_sum_numbers(1, 2, 3))


def make_monte_carlo_integral(P, x1, y1, x2, y2):
    store = {"count": 0, "fact": 0, "rect_area": (x2 - x1) * (y2 - y1)}

    def helper():
        x = random.uniform(x1, x2)
        y = random.uniform(y1, y2)
        return P(x, y)

    def trials(msg, *arg):
        if msg == "run trials":
            for x in range(arg[0]):
                store["count"] += 1
                if helper() == True:
                    store["fact"] += 1
        elif msg == "trials":
            return store["count"]
        elif msg == "get estimate":
            return (store["fact"] / store["count"]) * store["rect_area"]

        pass

    return trials
    pass
    ### FILL YOUR CODE HERE ###


### DO NOT MODIFY THIS ###
import math
import random


def circle(x, y):
    return math.sqrt(x * x + y * y) < 1


circle_estimate = make_monte_carlo_integral(circle, -1, -1, 1, 1)
circle_estimate("run trials", 1000)
print(circle_estimate("get estimate"))
circle_estimate("run trials", 10000)
print(circle_estimate("trials"))
### The inrange function in testcases is used to check whether a value lies in a specified range.


def translate(source, destination, string):
    store = {}
    for x in range(len(source)):
        store[source[x]] = destination[x]
    result = ""
    for x in string:
        if x in store.keys():
            result += store[x]
        else:
            result += x
    return result
    ### FILL YOUR CODE HERE ###


print(translate("dikn", "lvei", "My tutor IS kind"))
print(translate("(hrd", ")esy", "CODING is hard :("))
print(translate("", "", "CS1010S is awesome!!!"))


def caesar_cipher(shift, string):
    result = ""
    for c in string:
        # check if character is an uppercase letter
        if c.isupper():
            # find the position in 0-25
            c_unicode = ord(c)
            c_index = ord(c) - ord("A")
            # perform the shift
            new_index = (c_index + shift) % 26
            # convert to new character
            new_unicode = new_index + ord("A")
            new_character = chr(new_unicode)
            # append to encrypted string
            result = result + new_character

        else:  # char is lowercase
            # find the position in 0-25
            c_unicode = ord(c)
            c_index = ord(c) - ord("a")
            # perform the shift
            new_index = (c_index + shift) % 26
            # convert to new character
            new_unicode = new_index + ord("a")
            new_character = chr(new_unicode)
            # append to encrypted string
            result = result + new_character
        pass
    return result
    ### FILL YOUR CODE HERE ###


print(caesar_cipher(10, "abcd"))
print(caesar_cipher(25, "aAbB"))
print(caesar_cipher(25, ""))
