num = int(input("enter a numer = "));
rev = 0;
while num > 0:
    i= num % 10 ;
    
    rev = i + rev * 10
    num = num// 10
print(rev)
