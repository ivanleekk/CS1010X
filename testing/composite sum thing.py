##from math import *

##def f(n):
##    if n < 3:
##        return n
##    else:
##        return f(n-1) + 2*f(n-2)+3*f(n-3)
##    return
##
##def g(n):
##    g1 = 0
##    g2 = 1
##    g3 = 2
##    g4 = 0
##    if n < 3:
##        return n
##    
##    for x in range(3,n+1):
##        g4 = g3 + 2*g2 + 3*g1
##        g1,g2,g3 = g2,g3,g4
##        pass
##    return g4
##    
##
####for x in range(20):
####    print(f(x))
####
####for x in range(20):
####    print(g(x))
##
##def fib(n):
##    x = 0
##    y = 1
##    z = 0
##    for n in range(n):
##        z = x + y
##        x,y = y,z
##        pass
##    return z
##
##def is_fib(n):
##    if round(sqrt(5*n**2 + 4))**2 == 5*n**2 + 4  or round(sqrt(5*n**2 - 4))**2 == 5*n**2 - 4:
##        return True
##    else:
##        return False


##fib_list = []
##for x in range(20):
##    fib_list.append(fib(x))
##    print(fib(x))
##    print(is_fib(fib(x)))


##def fold2(op, term, a, next, b, base): 
##    if a > b:
##        return base
##    else:
##        return op (term(a), fold2(op, term, next(a), next, b, base))
##
##def geometric_series(a, r, n):
##    if r>1:
##        return fold2(lambda x,y: x+y, lambda z:z, a, lambda a:a*r, a*r**(n-1)-1,a*r**(n-1))
##    elif r<1:
##        return 1-fold2(lambda x,y: x+y, lambda z:z, a, lambda a:a*r, a*r**(n-1)-1,a*r**(n-1))
##    elif r == 1:
##        return a*n
##
##    
##
##
##print(geometric_series(1/2, 1/2, 3))



def num_combination(n, m):
    """Calculates number of ways to choose m items from a set of n distinct items"""
    if n == 0:
        return 0
    elif m == 0:
        return 1
    elif n == m:
        return 1
    return num_combination(n-1,m-1) + num_combination(n-1,m) 

    pass


print(num_combination(20, 4))		
print(num_combination(17, 5))
print(num_combination(5, 3))	
print(num_combination(5, 0))	
print(num_combination(0, 10))
