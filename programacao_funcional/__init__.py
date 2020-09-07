def fatorial_rec(m):
    if m == 0 or m == 1:
        return 1
    else:
        return m * fatorial_rec(m - 1)


print(fatorial_rec(4))