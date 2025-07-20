def replace_vowel(str):
    vowels = "aeiou"
    result = " "
    
    for chars in str:
        if chars in vowels:
            result += "*"
        else:
            result += chars
    return result

str = input("Enter string: ").lower()
output = replace_vowel(str)
print(output)      