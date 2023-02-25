def my_join(strings, separator):
    # initialize an empty result string
    result = ''
    
    # loop through the strings in the list
    for i, s in enumerate(strings):
        # add the separator before each string except the first one
        if i > 0:
            result += separator
        # add the string to the result
        result += s
    
    return result

    
 
niger = ["alio", "ohyeah"]
separator = ' '
ohyeao = my_join(niger,separator)

print(ohyeao)