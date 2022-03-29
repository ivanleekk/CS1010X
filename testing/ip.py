def ip_format(ip_address):
    group_1 = ip_address[0:8]
    group_2 = ip_address[8:16]
    group_3 = ip_address[16:24]
    group_4 = ip_address[24:32]
    
    def group_number(group):
        temp = 0
        for x in range(0,8):
            temp = temp + int(group[x])*(2**(7-x))
        return temp
    
    part_1 = group_number(group_1)
    part_2 = group_number(group_2)
    part_3 = group_number(group_3)
    part_4 = group_number(group_4)

    final = f"{part_1}.{part_2}.{part_3}.{part_4}"
    return final

ip_format('10100000111011011110101010111100')
