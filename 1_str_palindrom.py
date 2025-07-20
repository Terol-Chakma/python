# string palindrome
n=input("Enter a String: ")
reversed_str= n[::-1]
print(reversed_str)

if(reversed_str==n):
    print("The string ", n, " is Palindrome")
else:
    print("The string", n, " is Not Palindrome")

