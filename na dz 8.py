p = range(0,5)
it = iter(p)
a = [(1 + next(it)*5) for i in range(5)]
print(a)