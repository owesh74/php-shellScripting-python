num = int(input("enter a number = "))

num1 =( num // 100 ) % 10
num2 =( num // 10 ) % 10
num3 =( num % 10 )

cnum1= num1 * num1 * num1
cnum2= num2 * num2 * num2
cnum3=   num3 * num3 * num3
    
sumofc=(cnum1 + cnum2 + cnum3)

if(sumofc == num ):
    print(f"sum of cube of {num} is same {sumofc}.")
else:
    print(f"sum of cube of {num} is  not same {sumofc}.")

