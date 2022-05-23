
result = []
def divider(a, b):
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    return a/b
data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8 : 4}
for key in data:
    res = divider(key, data[kem])
    result.append(res)
class BLE(Exception):
    def __str__(self):
        
def ch(value):
    raise BLE()
ch()
print(result)