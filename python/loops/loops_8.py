min = int(input("enter start num="))
max = int(input("enter last num="))




for n in range(min,max+1):
    if n > 1:
        for i in range(2,n):
            if ( n % i ) == 0:
                break


        else:
            print(n)
