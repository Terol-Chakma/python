
marks = [58,23,16,32,75,99,45,18]

#slicing
#marks[1:4]#print(marks[-4:-1])

marks = marks[1:5]
marks = marks[:5]
marks = marks[-4:-1]
marks = marks[3:]
marks = marks[-2:]
print(marks)

#list methods
list = [2,5,3,1,6,8]
list.append(4)
list.sort()
list.sort(reverse=True)
list.reverse()
list.insert(1,7)    #1 is index and 7 is value
list.remove(1)      # i is value
list.pop(1)          # 1 is index

print (list)