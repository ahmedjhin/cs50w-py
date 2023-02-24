# use sys to stop exit the cod
import sys



x = (input(f"x: "))
y = (input(f"y: "))

    

def cheque(o,l):
    if o.isnumeric() and l.isnumeric():
        return True
    else:
        print("inter numbers pleas") 
    sys.exit()

cheque(x,y)

def makeINT(x,y):
    x = int(x)
    y = int(y)
    return x,y

x,y = makeINT(x,y)
    




try:
    result = x / y
except ZeroDivisionError:
    print("result = 0")
    sys.exit()
    
print(f"{x} / {y} = {result}")