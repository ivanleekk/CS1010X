#
# CS1010X --- Programming Methodology
#
# Mission 11b
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

# Collaborator: A0248890N Francis Chu

###############
# Mission 11b #
###############

##########
# Task 1 #
##########

# With these operations, compound generic operations can be defined, such as
def square(x):
    return mul(x, x)


# (a) What are the types of the input and output of the generic square operation?
# Answer: they are both generic numbers

# (b) Why would we prefer to define square in the above way, rather than:
# def square(x):
#    return apply_generic("square", x)
# Answer: by doing it this way, you have to define many special methods to things like square cube etc in the package, whereas in the previous way you can build them using the primitives like add, sub, mul and div which give you the same result for less work

##########
# Task 2 #
##########
# In the ordinary number package, a generic number operator is indexed by the
# name of the operator and a tuple of strings. For example, the add operator is
# indexed by ’add_ord’ and (’ordinary’, ’ordinary’); negation is indexed by
# ’negate_ord’ and (’ordinary’, ).
# In contrast, the constructor that creates an ordinary number is indexed by
# ’make_ord’ and just a string ’ordinary’. Explain why we have such a difference.

# Hint: Consider the differences in the process of the creation of a Generic-Num,
# such as create_ordinary, and the operations we can apply on Generic-Num, such
# as add. How is make_ord invoked, and how is add_ord invoked?

# Answer: when using an operator such as add or negate, you are working with a generic number that already
# has a tag applied on to it and the tuple comes from reading the tag of each number in the arguments,
# in the case of add(), 2 arguments which gives it ("ordinary", "ordinary") or in the case of negate(),
# 1 argument which gives it ("ordinary"). using these tags, apply generic uses a series of if statements
# to find which function to return and apply on the arguments, e.g. add_ord() or negate_ord() and use it
# on the given arguments in generic add or generic negate.

# However, for create_ordinary(), the input is not a generic number but a raw python number like an int or float.
# these numbers do not have tags and rather the tag with string "ordinary" comes from
# create_ordinary() which adds "ordinary" as the index to search for make_ord inside the make functions
# in order to apply it on to the raw number input from create_ordinary() to make a generic ordniary number

##########
# Task 3 #
##########

# There’s a right way and a wrong way to create a generic complex number. Here are two tries at
# producing 9+10i. Which is the right way?

# first_try = create_complex(9, 10)
# second_try = create_complex(create_ordinary(9), create_ordinary(10))

# What happens when you use the wrong way to produce 9+10i and 3+10i and then try to add
# them? Why does this happen?

# Right way: second way

# What happens: when you use the first way and try to add the numbers, you will get a "bad tagged datum" error

# Why it happens: This happens because in the complex number package, the basic operators such as "add",
# "sub", "mul" etc all call their generic counterparts inside the function to do the function such as adding
#  the real parts and imag parts together. But to call a generic add, you have to use a generic number, which
# is why using the first way will not work as the numbers are raw integers and not tagged, causing the generic
# operators to fail and give a "bad tagged datum error"

##########
# Task 4 #
##########

# Produce expressions that define c2_plus_7i to be the generic complex number whose real part is 2
# and whose imaginary part is 7, and c3_plus_1i to be the generic complex number whose real part
# is 3 and whose imaginary part is 1. Assume that the expression
# >>> csq = square(sub(c2_plus_7i, c3_plus_1i))
# is evaluated. Draw a box and pointer diagram that represents csq.

# As an example, the following is a box and pointer diagram that represents x, a Generic-
# Ord number:
# x = create_ordinary(5)
#
#         +---+---+---+---+
# x  -->  |       |       |
#         +---+---+---+---+
#             |       |
#             v       v
#         "ordinary"  5

# FILL IN YOUR ANSWERS HERE:
# c2_plus_7i = create_complex(create_ordinary(2), create_ordinary(7))
# c3_plus_1i = create_complex(create_ordinary(3), create_ordinary(1))


# csq = square(sub(c2_plus_7i, c3_plus_1i))

## Sample ASCII box and pointer diagrams (with 2 components) for your convenience
##            +---+---+---+---+
##            |   |   |    ---|--->
##            +---+---+---+---+
##                |
##                v

##            +---+---+---+---+
##            |   |   |   |   |
##            +---+---+---+---+
##                |       |
##                v       v

##########
# Task 5 #
##########

# Within the generic complex number package, the internal add_com function
# handled the addition operation. Why is it not
# possible to name this function "add"?

# Answer: if you name it "add", it will overwrite the generic_add function, which will prevent the add
# function from working for the other data types such as ordinary or rational numbers.

##########
# Task 6 #
##########

from generic_arith import *

# Modify install_complex_package, indicating clearly your modifications.
def install_complex_package():
    def make_com(x, y):
        return tag(repcom(x, y))

    def repcom(x, y):
        return (x, y)

    def real(x):
        return x[0]

    def imag(x):
        return x[1]

    def tag(x):
        return attach_tag("complex", x)

    # add, sub, mul, div: (RepCom, RepCom) -> Generic-Com
    def add_com(x, y):
        return make_com(add(real(x), real(y)), add(imag(x), imag(y)))

    def sub_com(x, y):
        return make_com(sub(real(x), real(y)), sub(imag(x), imag(y)))

    def mul_com(x, y):
        return make_com(
            sub(mul(real(x), real(y)), mul(imag(x), imag(y))),
            add(mul(real(x), imag(y)), mul(real(y), imag(x))),
        )

    def div_com(x, y):
        com_conj = content(complex_conjugate(y))
        x_times_com_conj = content(mul_com(x, com_conj))
        y_times_com_conj = content(mul_com(y, com_conj))
        return make_com(
            div(real(x_times_com_conj), real(y_times_com_conj)),
            div(imag(x_times_com_conj), real(y_times_com_conj)),
        )

    def complex_conjugate(x):
        return make_com(real(x), negate(imag(x)))

    # the 3 functions below are by me
    def negate_com(x):  # (rep-com) -> generic-com
        return make_com(negate(real(x)), negate(imag(x)))

    def is_zero_com(x):  # (rep-com) -> Boolean
        if real(x) == 0 and imag(x) == 0:
            return True
        else:
            return False

    def is_eq_com(x, y):  # (rep-com,rep-com) -> Boolean
        return x == y

    put("make", "complex", make_com)
    put("add", ("complex", "complex"), add_com)
    put("sub", ("complex", "complex"), sub_com)
    put("mul", ("complex", "complex"), mul_com)
    put("div", ("complex", "complex"), div_com)
    # added the 3 put statements below to allow generic functions to access these
    put("negate", ("complex",), negate_com)
    put("is_zero", ("complex",), is_zero_com)
    put("is_equal", ("complex", "complex"), is_eq_com)


install_complex_package()


def create_complex(x, y):
    return get("make", "complex")(x, y)


# Change the values for the test variables below
c_neg3_plus_10i = create_complex(create_ordinary(-3), create_ordinary(10))
c1_plus_2i = create_complex(create_ordinary(1), create_ordinary(2))
c1_plus_3i = create_complex(create_ordinary(1), create_ordinary(3))
# com1 = create_complex(1, 2)
# print(add(com1, com1))
print(c_neg3_plus_10i)
print(negate(c_neg3_plus_10i))
#################
# Do not change #
#################
def gradeThis():
    if is_equal(
        sub(c_neg3_plus_10i, mul(c1_plus_2i, c1_plus_3i)), add(c1_plus_2i, c1_plus_3i)
    ):
        print("Well done!")
    else:
        print("Please check your solution.")


gradeThis()

# c1 = create_complex(create_ordinary(2), create_ordinary(7))
# c2 = create_complex(create_ordinary(3), create_ordinary(1))
# print(square(sub(c1, c2)))
