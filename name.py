import sys

names = ("man" , "woman" , "child")

n = int(input("pick a number: "))

if n <= 2:
    print(names[n])
else:
    print("YOU STUPID")
    sys.exit

    
name = input("name: ")
print(f"hello {name}")



