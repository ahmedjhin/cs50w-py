names = ["ahmed", "ali", "raco"]


def print_name3(userInput: str):
    if validation(userInput):
        number = int(userInput)
        print(names [number - 1])
    else:
        print("worng")    
            

def validation(userInput: str) -> bool:
    if userInput.isnumeric() and 1 <= int(userInput) <= len(names):
        return True
    return False


print_name3(input("pick a number: "))