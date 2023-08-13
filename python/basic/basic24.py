mat = 50
sci = 50 
his = 50
eng = 50
mar = 50

total = mat + sci + his + eng + mar

per = (total/500) * 100

if( per >= 35 ):
    print(f"total marks of student {total} , total percentage {per}% , student is passed")
else:
    print(f"total marks of student {total} , total percentage {per}% , student is fail")
