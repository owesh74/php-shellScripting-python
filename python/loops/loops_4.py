#WAP to raed a number and find sum of all numbers from 1 to that number
num =int(input("enter a number="))
total=0
for i in range(1,num+1):
 
    total = total + i

print(f"sum of {num} is {total}")
