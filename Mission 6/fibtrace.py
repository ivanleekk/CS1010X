from diagnostic import *
from hi_graph_connect_ends import *

def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

##trace(fib)
##fib(3)
####untrace(fib)
##fib(3)

original_rotate = rotate
replace_fn(rotate,joe_rotate)

trace(x_of)
((gosper_curve(2)(0.5)))

##untrace(gosper_curve)
##gosper_curve(1)
