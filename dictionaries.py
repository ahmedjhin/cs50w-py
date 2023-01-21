houses = {
        "harry": "Griffindor",
        "Draco": "Slytherin",
        "ali": "chikago"
}


houses["amigos"] = "Griffindor"

keys = ["harry", "Draco", "ali"]

def keyfun(aop, aboki):
    for key in aop:
        print(f" {key} {aboki[key]}")



keyfun(keys,houses)


