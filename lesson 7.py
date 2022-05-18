import warnings
warnings.simplefilter("ignore" , SyntaxWarning)
warnings.simplefilter("always",ImportWarning)
warnings.warn("Warning, no code here",SyntaxWarning)
warnings.warn("Warning, module not import ",ImportWarning)





# class BLE(Exception):
#     def __str__(self):
#         return f"With so much material the house cannot be built!"
# def ch(amount_of_material, l):
#     if amount_of_material > l:
#         return "enough material"
#     else:
#         raise BLE(amount_of_material)
# materials = 123
# ch(materials,300)
#
#






# def checker(var1):
#     if type(var1) != str:
#         raise TypeError(f"Sorry, we can not work with {type(var1)}, we need class str")
#     else:
#         return var1
# fir = 10
# checker(fir)








# try:
#      print(k)
# except:
#     print("Something went wrong")
# else:
#     print("Else program do")
# finally:
#     print(" The Program has completed it`s work")
#
#















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