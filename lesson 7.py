try:
     print(k)
except:
    print("Something went wrong")
else:
    print("Else program do")
finally:
    print(" The Program has completed it`s work")

















# def division(a,b):
#         res = 0
#         try:
#             res = a/b
#
#         except:
#             try:
#                 a = int(a)
#                 b= int(b)
#                 res = a/b
#             except ZeroDivisionError:
#                 res = 0
#             except ValueError:
#                 res = 0
#             except ImportError:
#                 res = 0
#             except InterruptedError:
#                 res = 0
#             except KeyboardInterrupt:
#                 res = 0
#         print(res)
#
# while res == 0:
#     division(input("a = "),input("b = "))