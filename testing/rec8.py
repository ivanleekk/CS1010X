def make_stack():
    mem = []
    def stack(m):
        print(mem)
        if m == "is_empty":
            return not mem
        elif m == "clear":
            mem.clear()
        elif m == "peek":
            if mem == []:
                return None
            else:
                return mem[-1]
        elif m == "push":
            def push_stack(item):
                mem.append(item)
                pass
            return push_stack
        elif m == "pop":
            if mem == []:
                return None
            else:
                return mem.pop()
        else:
            print("command not recognised")
    return stack

def push_all(stack,seq):
    for x in range(len(seq)):
        stack("push")(seq.pop(0))
    return stack

def pop_all(stack):
    result= []
    while not stack("is_empty"):
        result.append(stack("pop"))
    return result

s = make_stack ()
print ( s ("is_empty")) # True
s ("push")( 1 )
s ("push")( 2 )
print ( s ("peek")) # 2
print (str( s ("pop"))) # 2
print (str( s ("pop"))) # 1
print (str( s ("pop"))) # None
print(push_all(s,list(range(10))))
print(s("is_empty"))
print(pop_all(s))


def make_calculator():
    stack = make_stack ()
    ops = {'+': lambda x , y : x + y ,
    '-': lambda x , y : x - y ,
    '*': lambda x , y : x * y ,
    '/': lambda x , y : x / y }

    def oplookup(msg, *num):
    # YOUR CODE BEGINS HERE
        if msg in ops.keys():
            return ops[msg]
        elif msg == "ANSWER":
            return stack("peek")
        elif msg == "CLEAR":
            pop_all(stack)
            pass
        elif msg == "NUMBER_INPUT":
            stack("push")(num[0])
            pass
        elif msg == "OPERATION_INPUT":
            op = oplookup(num[0])
            a = stack("pop")
            b=stack("pop")
            stack("push")(op(b,a))
            pass
        
    
    # YOUR CODE ENDS HERE
        else :
            raise Exception (" calculator doesn 't" + msg )
    return oplookup

c = make_calculator ()
print ( c ('ANSWER')) # empty_stack
print ( c ('NUMBER_INPUT',4 )) # pushed
print ( c ('ANSWER')) # 4
print ( c ('NUMBER_INPUT',5 )) # pushed
print ( c ('ANSWER')) # 5
print ( c ('OPERATION_INPUT','+')) # pushed
print ( c ('ANSWER')) # 9
print ( c ('NUMBER_INPUT',7 )) # pushed
print ( c ('OPERATION_INPUT','-')) # pushed
print ( c ('ANSWER')) # 2
print ( c ('CLEAR')) # cleared
print ( c ('ANSWER')) # empty_stack
