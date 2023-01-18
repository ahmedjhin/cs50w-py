player1 = input("your name: ")

data = []


def players(player):
    data.append(player)
    if player1 in data:
        return

players(player1)


s = ''

for i in data:
    s.append({i})
    

print(s)

str_1 = 'hello'

str_2 = 'world'

result = str_1 + ' ' + str_2

print(result)  # 👉️ 'hello world'
