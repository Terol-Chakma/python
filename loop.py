# while loop
i = 1               # i = 5
while i <=5:        # while i>=1:
    print("terol") #pt(i) || pt(i)
    i+=1            # i-=1
                    # pt("loop ended")

# Q. pt elements of following list 
nums = [1,4,9,16,25,36,49,64,81,100]
i = 0
while i <len(nums):
    #print(nums[i])
    i+=1

# Q. search a no x from given tuple
nums = [1,4,9,16,25,36,49,64,81,100]
x = 36
idx = 0
while idx < len(nums):
    #if(nums[idx] == x):
        #print("Item found at idx",idx)
    idx += 1
    
# Q. sum of first n numbers(while loop)
n = int(input("Enter number: "))
sum = 0
while(i<=n):
    sum += i
    print("The sum of first",n,"numbers :",sum)
    i+=1
    
# break & continue
#break
num = [1,4,9,16,25,36,49,64,81,100]
x = 36
i = 0
while i < len(num):
    if(nums[i] == x):
        print("Item found at idx",i)
        break               # when found, it will not execute further, stoppd here
    else:
        print("Finding...")
    i += 1
print("Loop ended")

#continue
i = 0
while i<=5:
    if(i==3):
        i+=1
        continue    # when  if( matched) it will skiped, that value will not print
    print(i)
    i+=1
    
# for loop
list = [1,2,3]
for el in list:
    print(el)
    
for el in list:
    print(el)
else:   #optional ; used for adding extra text at the end of execution.
    print("End")

# Q1. search element x from tuple
tup = (1,4,9,16,25,36,49,64,81,100)
x=49
idx = 0
for el in tup:
    if(el==x):
        print("Element found at idx",idx)
        break
    idx += 1

# range() in for loop
for el in range(1,7,2):     #start, stop, gap/step
    print(el)
    
# pass statement
for i in range(5):
    pass    # null statement, it states to move forward
print("END")

# Q. factorial of first n numbers
n = int(input("Enter number: "))
facto=1
for i in range(1,n+1):
    facto*=i
print("The factorial of",n, "is :",facto)