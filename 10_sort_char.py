def sort_chars(str):
    strs = str.split()
    sorted_str = ["".join(sorted(strs)) for char in strs]
    return " ".join(sorted_str)

str = input("Enter something: ")
result = sort_chars(str)
print(result)