def take_input():
    print("")
    print("what do you do?")
    response = input(":").lower()
    words = response.split()
    if len(words) > 2 or len(words) < 2:
        return "error"
    else:
        return words

def return_list_values(var_list):
    keys = []
    for each in var_list:
        keys.append(each[1])
    return keys