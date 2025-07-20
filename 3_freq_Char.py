# frequency of characters
# using dictionary

def freq_char(str):
    frequency = { }
    for char in str:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

str = input("Enter the string: ")
char_freq = freq_char(str)
print(char_freq)


# using collection.counter

# from collections import Counter

# s = "hello"
# freq = Counter(s)
# print(freq)
