num = 6383


a = num // 1000

b = (num // 100) % 10

c = (num // 10) % 10

d = num % 10 


sum = a + b + c + d


print(f"sum of {num} digit number is {sum}")
