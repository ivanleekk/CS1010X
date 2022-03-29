def get_nth_digit(k, n):
    k_list = []
    for x in range(0,6):
        k_list.append(str(k)[x])
        continue
    print(k_list)
    return int(k_list[(6-n)])
    pass

print(get_nth_digit(375416, 4))
print(get_nth_digit(987654, 1))
print(get_nth_digit(123456, 6))
