num =int(input("give a number: "))

n1 = (num // 100) % 10
n2 = num % 10
n3 = num % 1

rev = n3 * 100 + n2 * 10 +n1

if( num == rev ):
    print(f" {num} is palindrome number")
else:
    print(f" {num} is palindrome number")
