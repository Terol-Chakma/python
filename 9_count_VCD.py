def count(str):
    vowels = "aeiou"
    vcount = ccount = dcount = 0
    
    for chars in str:
        if chars.isdigit():
            dcount += 1
        elif chars.isalpha():
            if chars in vowels:
                vcount += 1
            else:
                ccount += 1
    return vcount, ccount, dcount

str = input("Enter something: ")
v, c, d = count(str)
print("vowels = ,",v, "consonant = ,",c, "digits = ",d)