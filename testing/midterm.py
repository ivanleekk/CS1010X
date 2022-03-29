# def f(x):
#     if x == 0:
#         return 0
#     result = 0
#     for x in range(20, 0, -2):
#         x = 10
#         result += x
#     print(result)


# x = 3
# y = 1
# x = f(x)
# print(x)
# print(not x)
# print(not None)

# word = "0101010101010101010101"  # len(word) = 22
# mask = "-------*------*-------"  # 7 "-" then "*" then 6 "-" then "*" then 7 "-"
# masking = ((11, -11), (6, -6), (3, -3), (2, -2), (1, -1))
# for i in range(0, 5):
#     word = word[0::2]+word[1::2]
#     maskedWord = word[0:masking[i][0]] + mask[masking[i][0]: masking[i][1]] + \
#         word[masking[i][1]:]
#     print(maskedWord)

# def comp(f, g):
#     return lambda g: f(f(g))


# def add2(x):
#     return x+2


# def add3(x):
#     return lambda x: x+3


# print(add3(add2)(8))
# print(add3((add2)(8))(88))
# print(comp(add3, add2)(8)(88))
# print(comp(add3(add2), add3(add2))(8))


# def A(n):

#     if n == 1:
#         return 1
#     else:
#         return n + B(n+1)


# def B(n):

#     if n == 1:
#         return 1
#     else:
#         return n + A(n//2)


# def A_itr(n):
#     if n == 0:
#         return 1
#     result = 0
#     while n != 1:

#         result += n
#         n += 1
#         if n == 1:
#             break

#         result += n
#         n = n//2
#         if n == 1:
#             break
#     result += 1
#     return result


# x = 100009123702-900012313213214314
# print(A(x))
# print(A_itr(x))
def sumT(t, term, next):
    print(t)
    if t == ():
        return ()
    else:
        print(term(t))
        return term(t) + sumT(next(t), term, next)


# def map(f, t):
#     return sumT(t, lambda t: (f(t[0]),), lambda t: t[1:])


# def transpose(M):
#     return sumT(M, lambda x: map(lambda y: y[0], x), lambda x: map(lambda y: y[1:], x))


# M = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
# N = ((1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12))

# transpose(M)
# transpose(N)

# def average(t1, t2, t3):
#     return sumT((t1, t2, t3), lambda x: (((x[0][0] + x[1][0] + x[2][0])/3),), lambda x: (x[0][1:], x[1][1:], x[2][1:]))


# average((3, 4, 5, 6), (1, 2, 3, 4), (2, 9, 4, 8))

def prefix_sum(t):
    return sumT(t, lambda x: (x[0],), lambda x: x[1:])


print(prefix_sum((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))
