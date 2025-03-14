#tup = (2,5,3,4,8,9)  #tuples are within paranthesis
# tup =tup.index(1)
# tup=tup.count(5)
# tup = tup[1:4]
# print(tup)

# Q. ask the user to enter names of theire 3 fav movies & store them in a list

# movies = []   #list
# movie1 = input("Enter the 1st movie: ")
# movies.append(movie1)

# movie2 = input("Enter the 2nd movie: ")
# movies.append(movie2)

# movie3 = input("Enter the 3rd movie: ")
# movies.append(movie3)

# print(movies)

# Q. check if a list contain a palindrom of element
list = [1,2,3]
list1 = list.copy()
list1.reverse()
if(list1==list):
    print("Palindrome")
else:
    print("Not palindrome")
