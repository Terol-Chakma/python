# set dont allow the same or duplicate value, repeate elements stored only once,
set1 = {1,2,3,"Terol","python"}
set2 = {2,3,4}
print(set1)
print(type(set1))
print(len(set1))
null_set = set()    #nul set ; not set = {}... its a dict.

#set method
set1.add(5)
set1.add("Chakma")
set1.remove(2)
set1.pop()
set1.clear()

set1.union(set2)
print(set1.union(set2))

set1.intersection(set2)
print(set1.intersection(set2))

print(set1)

#questions
#Q1. enter marks of 3 subs from the user and store in a dictionary. start with empty dict
#and add one by one. use sub name as key and marks as value.
marks = {}
x = int(input("Enter the obtained mark of CN : "))
marks.update({"CN" : x})
x = int(input("Enter the obtained mark of DBMS : "))
marks.update({"DBMS" : x})
x = int(input("Enter the obtained mark of OS : "))
marks.update({"OS" : x})
print(marks)

#Q2. figure out a way to store 9 and 9.0 as separate values in the set
values = {
    ("floate",9.0),("int",9) # built in datatype
}
print(values)