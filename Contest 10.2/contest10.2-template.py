#
# CS1010X --- Programming Methodology
#
# Contest 10.2 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from random import *
from puzzle_AI import *


def AI(mat):
    # replace the following line with your code
    return ('w', 'a', 's', 'd')[randint(0,3)]


# UNCOMMENT THE FOLLOWING LINES AND RUN TO WATCH YOUR SOLVER AT WORK
#game_logic['AI'] = AI
#gamegrid = GameGrid(game_logic)

# UNCOMMENT THE FOLLOWING LINE AND RUN TO GRADE YOUR SOLVER
# Note: Your solver is expected to produce only valid moves.
#get_average_AI_score(AI, True)
