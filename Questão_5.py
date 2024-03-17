def inverter_string(string):
    invert_string = ""

    for i in range(len(string) - 1, -1, -1):
        invert_string += string[i]

    return invert_string


string_orig = input("Digite para inverter: ")
string_invert = inverter_string(string_orig)
print("String original:", string_orig)
print("String invertida:", string_invert)
