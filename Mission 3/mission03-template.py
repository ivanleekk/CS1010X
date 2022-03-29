#
# CS1010X --- Programming Methodology
#
# Mission 3
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

###########
# Task 1a #
###########

def compose(f, g):
    return lambda x: f(g(x))


def thrice(f):
    return compose(f, compose(f, f))


def repeated(f, n):
    if n == 0:
        return identity
    else:
        return compose(f, repeated(f, n - 1))

# Your answer here:
# n =9

###########
# Task 1b #
###########


def identity(x): return x
def add1(x): return x + 1
def sq(x): return x**2

# print(thrice(thrice)(add1)(0))
# print(add1((add1)(6)))
# Explanation: Result is 33 because it starts from left to right, thrice(thrice) composes a function thrice(thrice(thrice(f(x)))) as the function f(x) is add1, it becomes thrice(thrice(thrice(add1))) and repeats add1 27 times onto the argument of 6 which gives you 33

# print(thrice(thrice)(identity)(compose))
# Explanation: it forms a function with the same functionality as compose. Because thrice(thrice)(identity) is equivilant to identity as identity returns the same value back when it is called. Thus, when thrice(thrice)(identity) calls compose, compose is returned.

# print(thrice(thrice)(sq)(1))
# 1
# Explanation: thrice(thrice) composes a function thrice(thrice(thrice(f(x)))) as the function f(x) is sq, it returns sq(sq(sq(...))) with 27 times of sq. However as the argument is (1) and 1 to the power of anything remains 1, the function returns 1

# print(thrice(thrice)(sq)(2))
# Explanation: Same as for (iii), however now that the argument is (2), it returns the square of the square of the square up to 27 times and gives a very large number.


###########
# Task 2a #
###########

def combine(f, op, n):
    result = f(0)
    for i in range(n):
        result = op(result, f(i))
    return result


def smiley_sum(t):
    def f(x):
        if x == 0:
            return 0
        else:
            return x**2

    def op(x, y):
        if y == 1:
            return x + y
        else:
            return x + 2*y

    n = t + 1

    # Do not modify this return statement
    return combine(f, op, n)

# print(smiley_sum(1))
# print(smiley_sum(2))
# print(smiley_sum(5))

###########
# Task 2b #
###########


def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


def new_fib(n):

    def f(x):
        if x == 0:
            return 0
        if x == 1 or x == 2:
            return 1
        else:
            f1 = 0
            f2 = 1
            for x in range(x-1):
                f3 = f1 + f2
                f1, f2 = f2, f3

            return f3

    def op(x, y):
        return y
    return combine(f, op, n+1)


"""
Or provide an explanation why this can't be done.
# answer here
This is a hacky method I feel, because it basically bypasses any use of combine. But any method I can think of already requires
me to first generate the value of the first n-1 fib numbers first by iteration or recursion or using a formula
which would make using combine to find the nth fib number redundant since I already have to know all previous values of fib numbers.
"""

result = 0
for x in range(20):
    result = result + fib(x)
    print(x)
    print(fib(x))
    print(new_fib(x))
    print(fib(x) == new_fib(x))
