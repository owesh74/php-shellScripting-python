salary = 10000

com1 = (salary * 10) / 100

com2 = (salary * 12) / 100

com3 = (salary * 15) / 100

if(salary <= 10000 ):
    print(f"comission is {com1}")
elif(salary >= 10000 and salary <= 20000):
    print(f"comission is {com2}")
else:
    print(f"comission is {com3}")
