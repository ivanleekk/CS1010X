def calc_integral(f, a, b, n):
    h = h_calc(a,b,n)
    k_list = range(n+1)
    result = 0
    for k in k_list:
        if k == 0 or k == n:
            result = result + f(a + k*h)
            
        elif k % 2 == 0:
            result = result + 2*f(a+k*h)
        elif k % 2 == 1:
            result = result + 4*f(a+k*h)
    return result *(h/3)

def h_calc(a,b,n):
    return (b-a)/n
    
print(calc_integral(lambda x: x*x*x, 0, 1, 100))
