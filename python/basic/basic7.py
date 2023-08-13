num=int(input("enter a 4 digit  number"))

a = num // 1000

b = (num // 100) % 10

c = (num // 10) % 10

d = (num % 10)


sum = d * 1000 + c * 100 + b * 10 + a * 1 


print (f"reverse of {num} is {sum}")

