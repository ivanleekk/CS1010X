def sumT(t, term, next):
    if t == ():
        return ()
    else:
        return term(t) + sumT(next(t), term, next)


def prefix_sum(t):
    return sumT(t, lambda t: (t[0],), lambda t: () if len(t) < 2 else (t[0]+t[1],) + t[2:])

    print(prefix_sum((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))


def map(f, t):
    return sumT(t, lambda t: (f(t[0]),), lambda t: t[1:])


def transpose(M):
    return sumT(M, lambda N: (map(lambda row: row[0], N),), lambda N: (map(lambda row: row[0], N),))


N = ((1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12))
print(transpose(N))
