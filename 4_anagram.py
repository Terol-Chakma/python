def anagram(str1, str2):
    return (sorted(str1) == sorted(str2))

if __name__ == '__main__':
    str1 = input("Enter the first string: ").lower()
    str2 = input("Enter the second string: ").lower()
    
    if(anagram(str1, str2)):
        print("These strings are anagram to each other")
    else:
        print("These strings are not anagram to each other")