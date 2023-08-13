ang1 = 50
ang2 = 60
ang3 = 70

tri = (ang1 + ang2 + ang3 )

if( tri == 180 ):
    if(ang1 == ang2 == ang3):
        print("triangle can be formed , triangle is equlateral triangle")
    elif(ang1 == 90 or ang2 == 90 or ang3 == 90 ):
        print("triangle can be formed , triangle is right angle triangle")
    else:
        print("triangle can be formed , triangle is isocelus triangle")
