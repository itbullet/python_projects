def rec(a):
    if a>0:
        print(a)
        rec(a-1)
        print(a)


rec(10)