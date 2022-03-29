from math import sqrt

def get_bigger_root(a, b, c):
    root_1 = round((-b+sqrt(b**2-4*a*c))/(2*a),2)
    root_2 = round((-b-sqrt(b**2-4*a*c))/(2*a),2)
    if root_1 > root_2:
        return root_1
    else:
        return root_2
    pass

print(get_bigger_root(1, -8, 15))
print(get_bigger_root(3, 11, 9))
