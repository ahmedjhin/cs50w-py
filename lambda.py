people = [
    {"name": "Harry", "house": "gryffindor"},
    {"name": "Cho"  , "house": "Ravenclaw" },
    {"name": "Draco", "house": "Slytherin" }
]

def f(person):
    return person["name"]





people.sort(key=lambda ago: ago["name"])

print(people)