import random

l = []
for i in range(0, 10):
    l.append(random.randint(-10, 10))
print(l)
a = [random.randint(-10, 10) % 2 for i in range(10)]
print(a)

# class Counter:
#     def __init__(self,MuxNum):
#         self.i = 0
#         self.muxnumber = MuxNum
#     def __iter__(self):
#         self.i = 0
#         return self
#     def __next__(self):
#         self.i += 1
#         if self.i>self.muxnumber:
#             raise StopIteration
#         return self.i
# count = Counter(int(input()))
# for elem in count:
#     print(elem)
#


# import random
# mylist = [random.randint(-10,10)for i in range(10)]
# print(mylist)
# it = iter(mylist)
# for i in mylist:
#     print(next(it)-2)
