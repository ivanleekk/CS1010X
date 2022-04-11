#
# CS1010X --- Programming Methodology
#
# Mission 9 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

###############
# Pre-defined #
###############

a = [6, 4, 2, 9, 10, 4, 2, 1, 3]

###################
# Helper function #
###################

def accumulate(fn, initial, seq):
    if not seq: # if seq is empty
        return initial
    else:
        return fn(seq[0], accumulate(fn, initial, seq[1:]))

###########
# Task 1a #
###########

# The enumerate function should be helpful for you here.
# It takes in a sequence (either a list or a tuple)
# and returns an iteration of pairs each of which
# contains the index of the element and the element itself.
# Here's how to use it.

# for i, elem in enumerate((4, 10, 1, 3)):
#     print("I am in the", i ,"position and I am", elem)
# 
# I am in the 0 position and I am 4
# I am in the 1 position and I am 10
# I am in the 2 position and I am 1
# I am in the 3 position and I am 3

def search(x, seq):
    index = 0
    for y in seq:
##        print(index)
        if x <= y:
            return index
        else: index += 1
    return index
    return

print("## Q1a ##")
print(search(-5, (1, 5, 10)))
# => 0
print(search(3, (1, 5, 10)))
# => 1
print(search(7, [1, 5, 10]))
# => 2
print(search(5, (1, 5, 10)))
# => 1
print(search(42, [1, 5, 10]))
# => 3
print(search(42, (-5, 1, 3, 5, 7, 10)))
# => 6

###########
# Task 1b #
###########

def binary_search(x, seq):
    half = len(seq)//2
    temp = half//2
    while True:
##        temp = temp // 2
        if temp == 0:
            temp = 1
        print(half)
        if half > len(seq)-1:
            return half
        elif half == 1:
            if x <= seq[0]:
                return 0
        if seq[half-1] < x <= seq[half]:
            return half
        elif x <= seq[half]:
            half -= temp
            temp = temp //2
        elif x > seq[half]:
            half += temp
            temp = temp //2
                
    pass

print("## Q1b ##")
print(binary_search(-5, (1, 5, 10)))
# => 0
print(binary_search(3, (1, 5, 10)))
# => 1
print(binary_search(7, [1, 5, 10]))
# => 2
print(binary_search(5, (1, 5, 10)))
# => 1
print(binary_search(42, [1, 5, 10]))
# => 3
print(binary_search(42, (-5, 1, 3, 5, 7, 10)))
# => 6
print(binary_search(9160423,tuple(range(100000000))))

###########
# Task 2a #
###########

def insert_list(x, lst):

    index = search(x,lst)
    lst.insert(index,x)
    return lst

print("## Q2a ##")
print(insert_list(2, [1, 5, 9]))
#=> [1, 2, 5, 9]
print(insert_list(10, [1, 5, 9]))
#=> [1, 5, 9, 10]
print(insert_list(5, [2, 6, 8]))
#=> [2, 5, 6, 8]

###########
# Task 2b #
###########

def insert_tup(x, tup):
    index = search(x,tup)
    new_tup = tup[:index]
    new_tup += (x,)
    new_tup += tup[index:]
    return new_tup

print("## Q2b ##")
print(insert_tup(2, (1, 5, 9)))
#=> (1, 2, 5, 9)
print(insert_tup(10, (1, 5, 9)))
#=> (1, 5, 9, 10)
print(insert_tup(5, (2, 6, 8)))
#=> (2, 5, 6, 8)

###########
# Task 2c #
###########

tup = (5, 4, 10)
output_tup = insert_tup(7, tup)
lst = [5, 4, 10]
output_lst = insert_list(7, lst)

print("## Q2c ##")
print(tup is output_tup)
#=> Output: False
print(tup == output_tup)
#=> Output: False

print(lst is output_lst)
#=> Output: True
print(lst == output_lst)
#=> Output: True
#=> Explain the outputs:
#=> for the tuples, as we are creating brand new tuples, the content and memory location of the output tuple is different from the original, hence causing both to be false
#=> for the lists as we are editing the original list and not creating a new one, the memory location for the output list and the original list is the same, causing (is) to be True and since the original list has been modified, the content is identical as well, causing (==) to be True as well


###########
# Task 3a #
###########

def sort_list(lst):
    new_lst = []
    for x in lst:
        insert_list(x,new_lst)

    return new_lst

print("## Q3a ##")
print(sort_list([9, 6, 2, 4, 5]))
#=> [2, 4, 5, 6, 9]
print(sort_list([42, 7, 6, -42, 0]))
#=> [-42, 0, 6, 7, 42]
print(sort_list(["soda", "cola", "sprite", "root beer", "apple cider"]))
#=> ['apple cider', 'cola', 'root beer', 'soda', 'sprite']
print(sort_list(["turtle", "penguin", "dog", "cat", "ant eater", "butterfly"]))
#=> ['ant eater', 'butterfly', 'cat', 'dog', 'penguin', 'turtle']

###########
# Task 3b #
###########

#=> Time complexity of sort_list:O(n^2)

###########
# Task 3c #
###########

def sort_tup(tup):
    result = ()
    for x in tup:
        result = insert_tup(x,result)
    return result

print("## Q3c ##")
print(sort_tup((9, 6, 2, 4, 5)))
#=> (2, 4, 5, 6, 9)
print(sort_tup((42, 7, 6, -42, 0)))
#=> (-42, 0, 6, 7, 42)
print(sort_tup(("soda", "cola", "sprite", "root beer", "apple cider")))
#=> ('apple cider', 'cola', 'root beer', 'soda', 'sprite')
print(sort_tup(("turtle", "penguin", "dog", "cat", "ant eater", "butterfly")))
#=> ('ant eater', 'butterfly', 'cat', 'dog', 'penguin', 'turtle')

###########
# Task 4a #
###########

import shelf

# Please uncomment the test function calls to see the animation

def insert_animate(block_pos, shelf, high):
    block = shelf.pop(block_pos)
    block_size = block.size
    for x in range(high):
        if block_size <= shelf[x].size:
            shelf.insert(x,block)
            return shelf

    shelf.insert(high,block)
        
    # optional to return shelf but we do this for debugging
    return shelf

# Test cases for insert_animate

def test_insert_animate():
    shelf.clear_window()
    s = shelf.init_shelf((2, 6, 1, 4, 8, 3, 9))
    print("## Q4a ##")
    print(insert_animate(0, s, 0))
    # => [Block size: 2, Block size: 6, Block size: 1, Block size: 4, Block size: 8, Block size: 3, Block size: 9]
    print(insert_animate(1, s, 1))
    # => [Block size: 2, Block size: 6, Block size: 1, Block size: 4, Block size: 8, Block size: 3, Block size: 9]
    print(insert_animate(2, s, 2))
    # => [Block size: 1, Block size: 2, Block size: 6, Block size: 4, Block size: 8, Block size: 3, Block size: 9]
    print(insert_animate(3, s, 3))
    # => [Block size: 1, Block size: 2, Block size: 4, Block size: 6, Block size: 8, Block size: 3, Block size: 9]
    print(insert_animate(6, s, 6))
    # => [Block size: 1, Block size: 2, Block size: 4, Block size: 6, Block size: 8, Block size: 3, Block size: 9]

# Uncomment function call to test insert_animate()
test_insert_animate()

###########
# Task 4b #
###########

def sort_me_animate(shelf):
    high = 1
    for x in range(len(shelf)-1):
        print(high)
        insert_animate(high,shelf,high)
        high+=1
        
    # optional to return shelf but we do this for debugging
    return shelf

# Test cases for sort_me_animate

def test_sort_me_animate():
    shelf.clear_window()
    s = shelf.init_shelf((5,2,6,9,1,4,8,3))
    print("## Q4b ##")
    print(sort_me_animate(s))
    # => [Block size: 1, Block size: 2, Block size: 3, Block size: 4, Block size: 5, Block size: 6, Block size: 8, Block size: 9]
    shelf.clear_window()
    s = shelf.init_shelf((4, 8, 2, 9, 3, 1, 2, 3, 4, 10, 7, 5, 6))
    print(sort_me_animate(s))
    # => [Block size: 1, Block size: 2, Block size: 2, Block size: 3, Block size: 3, Block size: 4, Block size: 4, Block size: 5, Block size: 6, Block size: 7, Block size: 8, Block size: 9, Block size: 10]

# Test case to catch mutation while sorting

def test_sort_me_with_duplicates():
    shelf.clear_window()
    s = shelf.init_shelf((6,1,3,4,1,3,2,4,5,3,6,3,2,5,6,5,2))
    print(sort_me_animate(s))
    # => [Block size: 1, Block size: 1, Block size: 2, Block size: 3, Block size: 3, Block size: 4]

# Uncomment function call to test sort_me_animate()
##test_sort_me_animate()
##test_sort_me_with_duplicates()
