#dictionary is used to stored data values in key:value pair, //mutable but not allow duplicate

dict = {
    "Name" : "Terol Chakma",
    "Sub" : ["Python", "Java", "C", "C++"], #list
    "Topics" : ("Dictionary", "Set"),   #tuple
    "Age" : 23,     #int
    "is_adult" : True,  #boolean
    "CGPA" : 8.9,   #float
    "Marks" : [78,89,91],   #tuple   
}
print(dict)     #all dictionary
print(dict["Name"])     # only name
print(dict["Topics"])   # only topics

# for changing
dict["Name"] = "Chakma Terol"   #Terol Chakma replaced by Chakma Terol
# anything can change like this way

# Nested Dictionary
Student = {     #dict-1
    "Name" : "Terol",
    "Subjects" : {  # dict-2
        "CN" : 78,
        "DBMS" : 88,
        "DSA" : 89,
    }
    # ................
    # ................
}

print(Student)  #All
print(Student["Subjects"])  # only all subjects from student
print(Student["Subjects"]["CN"])    # Only the value of CN

# dictionary methoids
Student.keys()  #returns all keys
print(Student.keys())   #all keys will return
print(list(Student.keys()))  #type casting

Student.values()    #returns all values
Student.items()    #returns all (key : value) pairs as tuple ()
print(Student.items())

Student.get("Name")    #returns the key according to value
print(Student.get("Name"))

#Student.update({"#new dict"})
Student.update({"City" : "Durgapur"})
print(Student)

# in case of get() is there in no exixting keys the output will be null