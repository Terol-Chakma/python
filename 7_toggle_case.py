# def toggle_case(str):
#     return str.swapcase()

# str = input("Enter something: ")
# result = toggle_case(str)
# print(result)

#dsa
def toggle_case(str):
    result = " "
    for chars in str:
        if chars.islower():
             result += chars.upper()
        elif chars.isupper():
            result += chars.lower()
        else:
            result += chars
    return result

str = input("Enter something: ")
new_str = toggle_case(str)
print(new_str)