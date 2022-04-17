def accumulate(op, init, seq):
    if not seq:
        return init
    else:
        return op(seq[0], accumulate(op, init, seq[1:]))

def accumulate_n(op, init, sequences):
    if (not sequences) or (not sequences[0]):
        return type(sequences)()
    else:
        return ([accumulate(op, init, [x[0] for x in sequences])] + accumulate_n(op, init, [x[1:] for x in sequences]))

# print(accumulate_n(lambda x,y: x+y, 0, [[1,2],[3,4],[5,6]]))
# print(accumulate_n(lambda x,y: x+y, 0, [[1,4],[5,7],[9,10]]))
# print(accumulate_n(lambda x,y: x+y, 0, [[9,8],[7,6],[5,4]]))
# print(accumulate_n(lambda x,y: x+y, 0, [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]))

# print()
# print(accumulate(lambda x,y: x+y, 0, [1,2,3]))

def col_sum(m):
    return accumulate_n(lambda x,y: x+y, 0,m)

# print(col_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))

def transpose(m):
    
    result = []
    for colummn in range(len(m[0])):
        temp = []
        for row in m:
            temp.append(row.pop(0))
        result.append(temp)
    return result
    pass

def row_sum(m):
    return accumulate_n(lambda x,y: x+y, 0, transpose(m))
    pass
    
# print(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))
# print(transpose([[1, 9, 3], [4, 6, 2], [9, 9, 9], [2, 1, 7]]))
# print(row_sum([[2, 4, 6], [8, 10, 12], [14, 16, 18], [20, 22, 24]]))
# print(row_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))

def count_sentence(sentence):
    length = len(sentence)
    result = 0
    for x in sentence:
        result += len(x)
    if length >=2:
        result += length - 1
    return [length,result]
    pass

# print(count_sentence([['C', 'S', '1', '0', '1', '0', 'S'], ['R', 'o', 'c', 'k', 's']]))
# print(count_sentence([['P', 'y', 't', 'h', 'o', 'n'], ['i', 's'], ['c', 'o', 'o', 'l']]))

def letter_count(sentence):
    result = {}
    for word in sentence:
        for letter in word:
            if letter not in result.keys():
                result[letter] = 1
            else:
                result[letter] += 1
    ans = [[key,result[key]] for key in result.keys()]
    return ans
    pass

# print(sorted(letter_count([['C', 'S', '1', '0', '1', '0', 'S'], ['R', 'o', 'c', 'k', 's']])))
# print(sorted(letter_count([['P', 'y', 't', 'h', 'o', 'n'], ['i', 's'], ['c', 'o', 'o', 'l']])))
# print(sorted(letter_count([['s', 'h', 'e'], ['l', 'i', 'k', 'e', 's'],['p', 'i', 'e', 's']])))
# print(type(letter_count([['s', 'h', 'e'], ['l', 'i', 'k', 'e', 's'],['p', 'i', 'e', 's']])))

def most_frequent_letters(sentence):
    if not sentence:
        return []
    all = letter_count(sentence)
    max_num = max([x[1] for x in all])
    result = [x[0] for x in all if x[1] == max_num]
    return result
    pass

# print(set(most_frequent_letters([['C', 'S', '1', '0', '1', '0', 'S'], ['R', 'o', 'c', 'k', 's']])))
# print(set(most_frequent_letters([['P', 'y', 't', 'h', 'o', 'n'], ['i', 's'], ['c', 'o', 'o', 'l']])))
# print(set(most_frequent_letters([['s', 'h', 'e'], ['l', 'i', 'k', 'e', 's'],['p', 'i', 'e', 's']])))

def make_queue():
    return []
    pass

def enqueue(q, item):
    q.append(item)
    pass

def dequeue(q):
    return q.pop(0)
    pass
    
def size(q):
    return len(q)
    pass
    

# q = make_queue()
# enqueue(q, 1)
# enqueue(q, 5)
# print(size(q))
# print(dequeue(q))

def who_wins(m, players):
    q = make_queue()
    count = 0
    for player in players:
            enqueue(q, player)
    while len(players) >=m:
        for x in q:
            player = dequeue(q)
            if count % m == 0 and count != 0:
                players.remove(player)
                count = -1
            else:
                enqueue(q, player)
            count +=1
    return players
    pass

print(set(who_wins(3, ['val', 'hel', 'jam', 'jin', 'tze', 'eli', 'zha', 'lic'])))
print(who_wins(2, ['poo', 'ste', 'sim', 'nic', 'luo', 'ibr', 'sie', 'zhu']))