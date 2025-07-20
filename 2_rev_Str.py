# using two pointer
def rev_str(str):
    char = list(str)
    left, right = 0, len(char) - 1  # initialization of two pointers
    while left < right:
        char[left], char[right] = char[right] , char[left]
        left+= 1
        right-=1 
    return " ".join(char)

str = input("Enter the sting: ")
reversed_str = rev_str(str)
print(reversed_str)