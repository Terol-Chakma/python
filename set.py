# set dont allow the same or duplicate value, repeate elements stored only once,
set1 = {1,2,3,"Terol","python"}
set2 = {2,3,4}
print(set1)
# print(type(set1))
# print(len(set1))

#null_set = set()    #nul set ; not set = {}... its a dict.

# set method
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

