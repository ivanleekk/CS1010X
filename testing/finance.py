def deposit(principal, interest, duration):
    for x in range(duration):
        principal += principal * interest
    return principal
    pass


# print(deposit(100, 0.05, 1))
# print(deposit(100, 0.05, 2))


def balance(principal, interest, payout, duration):
    for x in range(duration):
        principal += principal * interest - payout
    return principal
    pass


print(balance(100000, 0.01, 5000, 1))
print(balance(100000, 0.01, 5000, 2))


def new_balance(principal, gap, payout, duration):
    def newbalance(interest):
        a = principal
        a = deposit(principal, interest, gap - 1)

        a = balance(a, interest, payout, duration)

        return a

    return newbalance


# # e.g.
# print(new_balance(1000, 2, 100, 2)(0.1))
# print(new_balance(10000, 3, 1000, 3)(0.05))

import math


def find_cpf_rate():
    principal = 166000
    payout = 1280
    test = new_balance(principal, 121, payout, 240)
    count = 1
    x = 1
    while True:
        print("x:", x)
        print("test: ", test(x))
        print()
        if -0.0001 < test(x) < 0.0001:
            return round(((1 + x) ** 12) - 1, 4)
        else:
            count += 1
        if test(x) > 0:
            x -= 1 / count
        else:
            x += 1 / count

    pass


print((find_cpf_rate()))
