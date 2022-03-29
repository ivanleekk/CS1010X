#
# CS1010X --- Programming Methodology
#
# Mission 7 - Sidequest 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from lazy_susan import *

##########
# Task 1 #
##########

def solve_trivial_2(table):
    if check_solved(table):
        return
    else:
        flip_coins(table,(1,0))
        check_solved(table)
        return
    pass

# test:
##t2_1 = create_table(2)
##solve_trivial_2(t2_1)
##print(check_solved(t2_1))


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

##t2_1_run = create_table(2)
##run(t2_1_run, solve_trivial_2)

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

##t2_1_susan = create_table(2)
##Susan(t2_1_susan)

########################################################





##########
# Task 2 #
##########

def solve_trivial_4(table):
    state = get_table_state(table)
    flip_coins(table,state)
    check_solved(table)
    return
    
    pass

# test:
##t4_2 = create_table(4)
##solve_trivial_4(t4_2)
##print(check_solved(t4_2))


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

##t4_2_run = create_table(4)
##run(t4_2_run, solve_trivial_4)

######################################################## 
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

##t4_2_susan = create_table(4)
##Susan(t4_2_susan)

########################################################





##########
# Task 3 #
##########

def solve_2(table):
    if check_solved(table):
        return
    else:
        flip_coins(table,(1,0))
        check_solved(table)
        return
    pass

# test:
# t2_3 = create_table(2)
# solve_2(t2_3)
# print(check_solved(t2_3))


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

##t2_3_run = create_table(2)
##run(t2_3_run, solve_2)

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

# t2_3_susan = create_table(2)
# Susan(t2_3_susan)

########################################################





##########
# Task 4 #
##########

def solve_4(table):
    a = (1,0,1,0)
    b = (1,1,0,0)
    c = (1,0,0,0)
    for x in range(1,8):
        if check_solved(table):
            return
        if x == 4:
            flip_coins(table,c)
        if x%2 == 0:
            flip_coins(table,b)
        if x%2 == 1:
            flip_coins(table,a)           
    
    pass

# test:
##t4_4 = create_table(4)
##solve_4(t4_4)
##print(check_solved(t4_4))


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

##t4_4_run = create_table(4)
##run(t4_4_run, solve_4)

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

# t4_4_susan = create_table(4)
# Susan(t4_4_susan)

########################################################





##########
# Task 5 #
##########

def solve(table):
    size = get_table_size(table)
    x = 1
    if size == 2: # get power of 2
        x = 1
    else:
        while size != 2:
            size = size/2
            x+=1


    base = (1,0)
    moves = (base,)
##    print(moves)

    def tuple_double(tup):
        new_tup = ()
        for x in tup:
            y = x+x
            new_tup += (y,)

##        print(new_tup)
        return new_tup
##    print(tuple_double(tuple_double(moves)))

    def tuple_double_blank(tup):
        new_tup = ()
##        print(tup)
##        print(type(tup))
        for x in tup:
            num = len(x)
            z = (0,)*num
            new_tup += (x+z,)
        return new_tup

    def tuple_middle(x):
        x = x+1
        z = ((1,)*(2**(x)) + (0,)*(2**x),)
        return z
                
    
    for x in range(x-1):
        new_moves = tuple_double(moves)
        middle = tuple_middle(x)
        back = tuple_double_blank(moves)
        moves = new_moves + middle + back

##    print(len(moves))
    def algorithm_maker(moves):
        seq = (moves[0],)
        for x in range(len(moves)-1):
            seq = (seq + (moves[x+1],) + seq)
##            print(seq)
            pass
        
        return seq
        pass

        

        
##    print(algorithm_maker(moves))
##    print(len(algorithm_maker(moves)))
    seq = algorithm_maker(moves)
    count = 0
    for x in seq:
        count += 1
        if check_solved(table):
            return print(count)
        else:
            flip_coins(table,x)

    pass

# test:
##t4_5 = create_table(4)
##solve(t4_5)
##print(check_solved(t4_5))

##t4_4_run = create_table(16)
##run(t4_4_run, solve)

t8_5 = create_table(8)
solve(t8_5)
print(check_solved(t8_5))

##t16_5 = create_table(16)
##solve(t16_5)
##print(check_solved(t16_5))

# Note: It is not advisable to execute run() if the table is large.
