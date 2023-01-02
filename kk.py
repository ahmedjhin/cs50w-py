while True:
  # Prompt the user for input
  num = input("Enter a number 2 or below: ")

  # Check if the input is a valid number
  if num.isdigit():
    num = int(num)

    # Check if the number is 2 or below
    if num <= 2:
      break
  else:
    print("Invalid input. Please enter a valid number.")

# The number entered is 2 or below
names = ("abo", "osm", "gew")
print(names[num])
print("Thank you for entering a number 2 or below.")



human_bodies = ["man", "woman", "child"]  # 0, 1, 2


# def print_name(user_input: str):
#     # should be a number between 1 and 3 (including 1 and 3)
#     if user_input.isnumeric():
#         number = int(user_input)

#         count_bodies = len(human_bodies)
#         range_start = 1
#         range_end = count_bodies + 1
#         valid_numbers = range(range_start, range_end)
#         # valid_numbers = [1, 2, 3]

#         if number in valid_numbers:
#             index = number - 1

#             print(human_bodies[index])


def print_name3(user_input: str):
    if user_input.isnumeric():
        number = int(user_input)
        lowest_number = 1
        highest_number = len(human_bodies)

        if lowest_number <= number <= highest_number:
            print(human_bodies[number - 1])


def validate(user_input: str):
    if user_input.isnumeric() and 1 <= int(user_input) <= len(human_bodies):
        return True




print_name3(input("pick a number: "))

# def print_name2(user_input: str):
#     # range [1, 2, 3]
#     if user_input.isnumeric() and int(user_input) in range(1, len(human_bodies) + 1):
#         print(human_bodies[int(user_input) - 1])
