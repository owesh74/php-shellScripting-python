
import random

def hard():
    jackpot = random.randint(1,100)
    flag= False

    print("you have only 5 chance! ")
    for i in range(1,6):
        guess = int(input("guess a number: "))

        if(jackpot == guess):
            print("you win!")
            flag = True
            break
        if(jackpot < guess):
            print("enter a smaller number")
        else:
            print("enter a greater number")
    if flag == False:
        print (f"tumse na hopayega! jackpot number is {jackpot}")              
        

def medium():
    jackpot = random.randint(1,100)
    flag= False

    print("you have 10 chance! ")
    for i in range(1,11):
        guess = int(input("guess a number: "))

        if(jackpot == guess):
            print("you win!")
            flag = True
            break
        if(jackpot < guess):
            print("enter a smaller number")
        else:
            print("enter a greater number")
    if flag == False:
        print (f"tumse na hopayega! jackpot number is {jackpot}")




def easy():
    jackpot = random.randint(1,100)
    flag= False
    print("you have 20 chance! ")
    for i in range(1,21):
        guess=int(input("guess a number: "))

        if(jackpot == guess):
            print("you win!")
            flag = True
            break
        if(jackpot < guess):
            print("enter a smaller number")
        else:
            print("enter a greater number")
    if flag == False:
       print (f"tumse na hopayega! jackpot number is {jackpot}")              




option = None;


print("===============+");
print("1. easy        |");
print("2. medium      |");
print("3. hard        |");
print("4. exit        |")
print("===============+")
option = int(input("Choose Option: "));

            
if(option == 1):
    easy();

                                                        
elif(option == 2):
    medium();


elif(option == 3):
    hard();                                         
        
elif(option == 4):
    print("exit")

else:
    print("invalid option")
