string = input("Digite uma palavra: ")

def inverter_string(s):
    if s == "":
        return ""
    return s[-1] + inverter_string(s[:-1])

print(inverter_string(string))