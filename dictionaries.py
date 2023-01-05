houses = {
        "harry": "Griffindor",
        "Draco": "Slytherin",
        "ali": "chikago"        
}
housaes = {
        "hassrry": "Grifssssssssssfindor",
        "Dracssssssso": "Slsssssytherin",
        "alssssssssssi": "chissssssskago"        
}


keys = ["harry", "Draco", "ali"]

keyss = ["hassrry", "Dracssssssso", "alssssssssssi"]
def keyfun(aboki, aop):
    for key in aop:
        print(f"{key}: {aboki[key]}")



keyfun(housaes,keyss)


def square(x):
    aio = x * x 
    aiol = aio + 11
    return aiol 

for i in range(1,10):
    print(f"we have {i} {square(i)} aloha")
