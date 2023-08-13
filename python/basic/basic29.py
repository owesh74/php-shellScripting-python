
maths = int(input("Enter marks in maths: "))
science = int(input("Enter marks in science: "))
history = int(input("Enter marks in history: "))
english = int(input("Enter marks in english: "))
marathi = int(input("Enter marks in marathi: "))
                                                      

if(maths>=0 and maths<=100 and science>=0 and science<=100 and history>=0 and history<=100 and english>=0 and english<=100 and marathi>=0 and marathi<=100):

        tot = maths + science + history + english + marathi
        per = tot/5
        print(f"total marks = {tot}")
        print(f"total percentage = {per} ")


        if(maths>=35 and science>=35 and history>=35 and english>=35 and marathi>=35):
                                                
            if(per>=75):
                print("Student is passed with 1st class Distinction ")
            elif(per>=60 and per<=75):
                print("Student is passed with 1st class")
            elif(per>=50 and per<=60):
                print("Student is passed with 2nd class")
            elif(per>=40 and per<=50):
                print("Student is passed with 3rd class")
            else:
                print("student is fail")
        else:
            print("student is fail")
else:
    print("invalid marks")

