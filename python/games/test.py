num = [[ 1 , 2 , 3 ]]
num1 =[[ 4 , 5 , 6 ]]
num2 =[[7 , 8 , 9 ]]
    
print(num)
print(num1)
print(num2)
for i in range(1, 4):

    n = int(input("player 1 chance="))
    

    if((n-1) % 2 == 0):
        num[0][n-1]= "X"
    elif((n-1)% 2 != 0 ):
        num[0][n-1]= "O"

    print(num)
    print(num1) 
    print(num2) 
        
for i in range(1, 4):

    n = int(input("player 1 chance="))


    if((n-1) % 2 == 0):
        num[0][n-1]= "X"
    elif((n-1)% 2 != 0 ):
        num[0][n-1]= "O"

    print(num) 
    print(num1) 
    print(num2) 
