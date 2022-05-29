import random
import logging

r = range(0,10)
it =iter(r)
l = [3+8*(next(it)) for i in r]
it = iter(l)
print(l)
logging.basicConfig(level=logging.ERROR, filename="logs.log", filemode="w",format="We have next logging messange:%(asctime)s%(levelname)s - %(message)s")
for i in l:
    try:
        print(l[next(it)]/random.randint(-5,5))
    except:
        logging.error("ZeroDivisionError")