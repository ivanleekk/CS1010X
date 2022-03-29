def hanoi(n, src, dsc, aux):
    result = ()
    if n == 1:
        result += ((src,dsc),)
        return result
    else: 
        result += hanoi(n-1, src, aux, dsc)
        result += (src,dsc),
        result += hanoi(n-1, aux, dsc, src)
    return result
    pass


print(hanoi(3,'A','B','C'))
