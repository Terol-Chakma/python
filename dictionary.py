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
#print(Student)  #All
#print(Student["Subjects"])  # only all subjects from student
print(Student["Subjects"]["CN"])