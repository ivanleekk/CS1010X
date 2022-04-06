def transpose(matrix):
    temp = []
    length = len(matrix[0])
    print(length)
    for x in range(length):
        temp.append([])
        for y in matrix:
            temp[x].append(y[x])
    print(temp)
    matrix.clear()
    for x in range(length):
        matrix.append(temp[x])
    return matrix
    pass


### DO NOT MODIFY THIS ###
# matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# matrix3 = [[1, 2, 3]]

# a = transpose(matrix1)
# b = transpose(matrix2)
# c = transpose(matrix3)
# print(a)
# print(b)
# print(c)

# print(a is matrix1)
# print(b is matrix2)
# print(c is matrix3)


def mode_score(students):
    scores = []
    for x in range(len(students)):
        scores.append(students[x][2])
    set_score = set(scores)
    count = dict.fromkeys(set_score, 0)
    for x in scores:
        count[x] += 1
    print(count)
    max_num = max(count.values())
    print(max_num)
    result = []
    for x in count:
        if count[x] == max_num:
            result.append(x)

    return result
    pass


def top_k(students, k):
    def get_score(student):
        return student[2]

    def get_name(student):
        return student[0]

    students.sort(key=get_name)
    students.sort(key=get_score, reverse=True)
    results = []
    for student in students:
        if get_score(student) >= get_score(students[k - 1]):
            results.append(student)
    return results
    pass


### DO NOT MODIFY THIS ###
students = [
    ("tiffany", "A", 15),
    ("jane", "B", 10),
    ("ben", "C", 8),
    ("simon", "A", 21),
    ("eugene", "A", 21),
    ("john", "A", 15),
    ("jimmy", "F", 1),
    ("charles", "C", 9),
    ("freddy", "D", 4),
    ("dave", "B", 12),
]

# print(set(mode_score(students)))
# print(
#     mode_score(
#         [("Dave", "A", 16), ("jane", "B", 10), ("Eugene", "A", 16), ("jimmy", "F", 1)]
#     )
# )

print(top_k(students, 5))
print(top_k(students, 3))
