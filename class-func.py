def get_full_name(employee):
    return f'{employee["first_name"]} {employee["last_name"]}'

def creat_employee(first_name, last_name, get_full_name_func):
    d = {"first_name": first_name, "last_name": last_name, "get_full_name": get_full_name_func}
    return d

e = creat_employee("Vera", "Schmidt", get_full_name)
print(e["get_full_name"](e))