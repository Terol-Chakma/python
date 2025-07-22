def remove_space(str):
    return " ".join(str.split())

str = input("Enter any sentence: ")
result = remove_space(str)
print(result)