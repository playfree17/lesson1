n = str(input("Enter a number: "))
x = [int(a) for a in str(n)]
k = 0
for i in x:
    if i == 2:
        k += 1
if k >=1:
    print("Yes")
else:
    print("No")