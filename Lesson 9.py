import logging
import os
x = 5
y = 8
z = 9
print(f"x = {x} y = {y} z = {z}")
print()
try:
    print(5/0)
except ZeroDivisionError:
    print("ZeroDivisionError")
logging.basicConfig(level=logging.DEBUG,filename="logs.log",filemode="w",format="We have next logging messange:%(asctime)s%(level name)s - %(message)s")
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")
logging.debug("debug")
logging.info("info")
# a = open("critical.log","w")
# a.write(logging.critical("critical"))
# a.close()