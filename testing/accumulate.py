def accumulate(combiner, base, term, a, next, b):
    if a <= b:
        return combiner(term(a), accumulate(combiner, base, term, next(a), next, b))
    else:
        return base


def sum(term, a, next, b):
    return accumulate(lambda x,y: x+y , 0 ,term, a, next, b)

##print(sum(lambda x: x*2, 1, lambda x: x+1, 5))
##print(sum(lambda x: x*2, 0, lambda x: x+2, 10))
##print(sum(lambda x: x**2, 1, lambda x: x+1, 5))

##def accumulate_iter(combiner, null_value, term, a, next, b):
##    result = null_value
##    for x in range(b):
##        if a <= b:
##            result = combiner(result, term(a))
##            a = next(a)
##    return result
##    pass

def accumulate_iter(combiner, null_value, term, a, next, b):

    list_a = ()
    y = a
    for x in range (b):
        if y <= b:
            list_a =  list_a + (y,)
            y = next(y)
    list_b = list_a[::-1]
##    result = combiner(list_b[0],null_value)
    result = null_value
    for x in list_b:

        result = combiner(term(x), result)


        
    return result
##    print (list_b)
##    print (list_a)
    pass

##print(accumulate_iter(lambda x,y: x*y, 1, lambda x: x*x, 1, lambda x: x+1, 5))
##print(accumulate_iter(lambda x, y: x*y, 1, lambda x: x**2 + 1, 0, lambda x: x+2, 5))
##
##print(accumulate_iter(lambda x, y: x+y, 1, lambda x: x**2 + 1, 0, lambda x: x+2, 5))


def remove_extras(lst):
    holding = []
    keep = []
    for x in range(len(lst)):
        if lst[x] in keep:
            holding.append(x)
        else:
            keep.append(lst[x])
    for x in holding[::-1]:
        lst.pop(x)
    return lst
    pass
    
# Do not remove the following code
lst1 = [1, 5, 1, 1, 3]
lst2 = [2, 2, 2, 1, 5, 4, 4]
result1 = remove_extras(lst1)
result2 = remove_extras(lst2)

##print(lst1)
##print(lst2)


##def sort_age(lst):
##    def check_false():
##        for x in range(len(lst)-1):
##            if lst[x][1] < lst[x+1][1]:
##                return True
##        return False
##    def sorting():
##        for x in range(len(lst)-1):
##            if lst[x][1] < lst[x+1][1]:
##                lst[x], lst [x+1] = lst[x+1], lst[x]
##    for x in range(len(lst)-1):
##        if check_false():
##            sorting()
##    return lst
##    pass

def sort_by_gender_then_age(lst):
    male = []
    female = []
    for x in lst:
        if x[0] == 'M':
            male.append(x)
        elif x[0] == 'F':
            female.append(x)
            
    def sort_age(lst):
        def check_false():
            for x in range(len(lst)-1):
                if lst[x][1] < lst[x+1][1]:
                    return True
            return False
        def sorting():
            for x in range(len(lst)-1):
                if lst[x][1] < lst[x+1][1]:
                    lst[x], lst [x+1] = lst[x+1], lst[x]
        for x in range(len(lst)-1):
            if check_false():
                sorting()
        return lst
        
    sort_age(male)
    sort_age(female)
    result = male + female
    return result



##print(sort_by_gender_then_age([("M", 23), ("F", 19), ("M", 30)]))
##print(sort_by_gender_then_age([("F", 18), ("M", 23), ("F", 19), ("M", 30)]))		
##print(sort_by_gender_then_age([("F", 18), ("M", 23), ("F", 19), ("M", 30), ("M", 17)]))	
##print(sort_by_gender_then_age([("M", 35), ("F", 18), ("M", 23), ("F", 19), ("M", 30), ("M", 17)]))		
##print(sort_by_gender_then_age([("F", 19)]))

##print([1,2,3,4,1,2,3,4]/2)


def merge_lists(list1, list2):
    result = []
    while list1 != [] and list2 != []:
        if list1[0]>= list2[0]:
            result.append(list1.pop(0))
        elif list2[0]>= list1[0]:
            result.append(list2.pop(0))
    if list1 == []:
        result += list2
    elif list2 == []:
        result += list1
    print(result)
    return result
    pass

##merge_lists([4, 2, 1], [6, 5, 3])	
##merge_lists([6, 4, 2, 1], [5, 3])	
##merge_lists([6, 5, 4, 2, 1], [])
##merge_lists([6, 5, 4, -1], [-2, -3])
##merge_lists([6, 5, 4, -1], [6, -2, -3])
