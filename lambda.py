person = [
    {"name": "Harry", "house": "gryffindor"},
    {"name": "Cho"  , "house": "Ravenclaw" },
    {"name": "Draco", "house": "Slytherin" }
]



person.sort(key=lambda ago: ago["name"])

print(person)