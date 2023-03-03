# use sys to stop exit the cod
import sys


try:
    x = int(input(f"x: "))
    y = int(input(f"y: "))
except ValueError:
    print("Error: Invalid input.")
    sys.exit()    

# def cheque(o,l):
#     if o.isnumeric() and l.isnumeric():
#         return True
#     else:
#         print("inter numbers pleas") 
#     sys.exit()

# cheque(x,y)

# def makeINT(x,y):
#     x = int(x)
#     y = int(y)
#     return x,y

# x,y = makeINT(x,y)
    




try:
    result = x / y
except ZeroDivisionError:
    print("result = 0")
    sys.exit(1)
    
print(f"{x} / {y} = {result}")