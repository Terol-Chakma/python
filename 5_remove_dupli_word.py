def rmv_dupli_word(str):
    char = set((str.lower()).split())
    return " ".join(char)
str = input("Enter the string: ")
new_str = rmv_dupli_word(str)
print(new_str)