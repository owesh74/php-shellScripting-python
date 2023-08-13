num = int(input("enter a number= "))

is_prime = True

for i in range (2,num):
    #print(num % i == 0)
    if(num % i ==0):
        is_prime = False
        break


if(is_prime == True):
    print(f"{num} is prime number ") 
else:
    print(f"{num} is not prime number ")


