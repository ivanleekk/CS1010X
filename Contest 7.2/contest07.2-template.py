#
# CS1010X --- Programming Methodology
#
# Contest 7.2 Template

from email.mime import base
from more_lazy_susan import *


# def create_solver(coins):  # score: 12017038 for 10:3411368
#     def solver(move_id):
#         m_id = move_id % coins
#         move = [False] * coins
#         move[m_id] = True
#         return move

#     return solver


# def create_solver(coins):  # score: 9379692
#     def solver(move_id):
#         if move_id % 3 == 0:
#             move = [True, False, False] * coins
#             pass
#         elif move_id % 3 == 1:
#             move = [False, True, False] * coins
#             pass
#         else:
#             move = [False, False, True] * coins
#             pass
#         return move

#     return solver


# def create_solver(coins):  # score: 12288990 for 10:3517211 score for 13:5452312
#     def solver(move_id):
#         move = [False] * coins
#         if move_id == 0:
#             move[0] = True
#             return move
#         for x in range(1, coins - 1):
#             if move_id % x == 0:
#                 move[x] = True
#         return move

#     return solver


# def create_solver(coins):  # score: 12869620 for 10:3461262 score for 13:5765296
#     def solver(move_id):
#         move = [True] * coins
#         if move_id == 0:
#             move[0] = False
#             return move
#         for x in range(1, coins - 1):
#             if move_id % x == 0:
#                 move[x] = False
#         return move

#     return solver


# def create_solver(coins):  # score: for 10:2918259
#     def solver1(move_id):
#         base1 = [True, False]
#         base2 = [False, True]
#         mid = coins // 2
#         if (move_id // coins) % 3 == 0:
#             move = base1 * mid
#         elif (move_id // coins) % 3 == 1:
#             move = base2 * (mid // 2)
#         else:
#             move = [True] * mid + [False] * (mid + 1)
#         return move

#     def solver2(move_id):
#         def flip(move, x):
#             move[x] = secrets.choice([True, False])

#         move = []
#         for x in range(coins):
#             move.append(secrets.choice([True, False]))

#     if coins == 10:
#         return solver1
#     else:
#         return solver2


# def create_solver(coins):  # score: 12388129 score for 10: 3497953 score for 13:6006384
#     def solver(move_id):
#         def flip(move, x):
#             if move[x] == True:
#                 move[x] = False
#             else:
#                 move[x] = True
#             pass

#         move = [True] * coins
#         if move_id == 0:
#             move[0] = False
#             return move
#         for x in range(1, coins - 1):
#             if move_id % x == 0:
#                 flip(move, x)
#                 flip(move, x - 2)
#             if move_id * coins % x == 0:
#                 flip(move, x)
#         return move

#     return solver


# def create_solver(coins):  # score:12390799 #score for 13:5589476
#     def solver(move_id):
#         def flip(move, x):
#             if move[x] == True:
#                 move[x] = False
#             else:
#                 move[x] = True
#             pass

#         move = [True] * coins
#         for y in range(move_id % 20):
#             to_change = secrets.randbelow(coins)
#             for x in range(to_change):
#                 flip(move, secrets.randbelow(coins))
#         return move

#     return solver


# def create_solver(coins):  # score:11675510
#     def solver(move_id):
#         def flip(move, x):
#             if move[x] == True:
#                 move[x] = False
#             else:
#                 move[x] = True

#         move = [True] * coins
#         for y in range(move_id % coins):
#             to_change = secrets.randbelow(coins // 2)
#             for x in range(to_change):
#                 flip(move, secrets.randbelow(coins))
#         return move

#     return solver


# def create_solver(coins):  # score: 12105290 for 10:3501730 for 13:5855212
#     def solver(move_id):
#         move = [False] * coins
#         for x in range(1, coins):
#             if move_id % x == 0:
#                 move[x] = True
#         return move

#     return solver


# def create_solver(coins):  # score: 12610726 for 10:3481158 for 13:5918628
#     def solver(move_id):
#         move = []
#         for x in range(coins):
#             move.append(secrets.choice([True, False]))

#     return solver


def create_solver(coins):  # score: 12474559 for 10:3479936 score for 15:3169621
    def solver(move_id):
        def flip(move, x):
            move[x] = secrets.choice([True, False])

        move = []
        for x in range(coins - 1):
            if move_id % 2 == 0:
                if x / coins < 0.5:
                    move.append(secrets.choice([True, False]))
                else:
                    move.append(False)
            else:
                if x / coins > 0.5:
                    move.append(secrets.choice([True, False]))
                else:
                    move.append(False)

    return solver


# def create_solver(coins):  # score: 10642286 score for 15:2924621
#     def solver(move_id):
#         to = secrets.randbelow(move_id % coins + 1)
#         move = [True] * to + [False] * (coins - to)
#         return move

#     return solver


# def create_solver(coins):  # score: 11041568 score for 15:2727298
#     def solver(move_id):
#         to = move_id % coins + 1
#         move = [True] * to + [False] * (coins - to)
#         return move

#     return solver


# def create_solver(coins):  # score:7561646 score for 15:1718059
#     def solver(move_id):
#         def flip(move, x):
#             move[x] = secrets.choice([True, False])

#         to = move_id % coins
#         move = [False] * coins
#         flip(move, to)
#         return move

#     return solver


# def create_solver(coins):
#     def solver1(move_id):  # score: for 10: 3500217
#         move = [False] * coins
#         if move_id == 0:
#             move[0] = True
#             return move
#         for x in range(1, coins - 1):
#             if move_id % x == 0:
#                 move[x] = True
#         return move

#     def solver2(move_id):  # score for 13:5996052
#         def flip(move, x):
#             if move[x] == True:
#                 move[x] = False
#             else:
#                 move[x] = True
#             pass

#         move = [True] * coins
#         if move_id == 0:
#             move[0] = False
#             return move
#         for x in range(1, coins - 1):
#             if move_id % x == 0:
#                 flip(move, x)
#                 flip(move, x - 2)
#             if move_id * coins % x == 0:
#                 flip(move, x)

#     def solver3(move_id):
#         def flip(move, x):
#             move[x] = secrets.choice([True, False])

#         move = []
#         for x in range(coins):
#             move.append(secrets.choice([True, False]))

#     if coins == 10:
#         return solver1
#     elif coins == 13:
#         return solver2
#     elif coins == 15:
#         return solver3


# UNCOMMENT THE FOLLOWING LINE AND RUN TO GRADE YOUR SOLVER
get_contest_score(create_solver, True)
