def is_sum_odd(num):
    digits = []
    string_name = str(num)
    print(type(digits))
    print(type(string_name))
    print(len(string_name))
    for x in range(0,len(string_name)):
        digits.append(string_name[x])
        continue
    print(digits[0])
    sum_of_digit = 0
    for x in range(0,len(digits)):
        
        sum_of_digit = sum_of_digit + int(digits[x])
        continue
    print(sum_of_digit)
    if sum_of_digit % 2 == 0:
        return False
        
    else:
        return True
    pass


print(is_sum_odd(12))
