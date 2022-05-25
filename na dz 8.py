p = range(0,10)
it = iter(p)
a = [(1 + next(it)*5) for i in range(10)]
print(a)
