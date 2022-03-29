def copy_tree(tree):
    if tree == ():
        return ()
    new_tpl = ()
    for x in tree:
        if type(x) == tuple:
            y = copy_tree(x)
            print(y)
            new_tpl += (y,)
        else:
            new_tpl += (x,)

  
    return new_tpl
    pass

# Do not remove this line
original = (1, 2, 3, 4)
test = (1,2,(3,4))
test2 = ()

##print(original is copy_tree(original))
##print(copy_tree(original))
##print(original is copy_tree(test))
##print(copy_tree(test))


##def count_leaves(tree):
##    if tree == ():
##        return 0
##    elif is_leaf(tree):
##        return 1
##    else:
##        return count_leaves(tree[0]) + count_leaves(tree[1:])
##
##x = ((1, 2), ((3, 4), (5, (6, 7), (8, 9))), (10, (11, 12)), (13, (14,), (16,), 17, 18, (19, 20)))
##print(count_leaves(x))

def pop_at_index(seq, index):
    new_tup = ()
    
    if index >= 0:
        a=0
        for x in range(len(seq)):
            if a == index:
                a+=1
            else:
                new_tup += (seq[x],)
                a+=1
    elif index < 0:
        a=-1
        for x in range(len(seq)):
##            print(a)
            if a == index:
                a-=1
            else:
##                print(seq[a])
                new_tup = (seq[a],) + new_tup
                a -= 1
    return new_tup
    pass

print(pop_at_index((1, 3, 5, 7), 0))
print(pop_at_index((1, 3, 5, 7), -2))		
print(pop_at_index((2, 4, 6, 8, 10), -4))	
print(pop_at_index((2, 4, 6, 8, 10), -10))
print(pop_at_index((1, ), 0)	)	
print(pop_at_index((1, 2, 3), -1))	
print(pop_at_index((1, 2, 3), 3))
