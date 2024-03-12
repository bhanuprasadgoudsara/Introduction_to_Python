# Check Leap year:
def check_leap_year(year):
    if year % 4 == 0:
        if year % 400 == 0:   # (year % 4 == 0 and year % 400 = 0)  --- True
            return True
        elif year % 100 == 0: # (year % 4 == 0 and year % 100 != 0) --- True
            return False
        else:                 # ( (year % 4 == 0) and (year % 400 != 0) and (year % 100 != 0) ) --- True
            return True
    else:
        return False
'''
a = int(input("Enter a year to check Leap Year: "))
if check_leap_year(a):
    print("%a is leap year" %a)
else:
    print("%a is not a leap year" %a)
'''

# Maximum Number out of Three
def max_of_three(a,b,c):
    print("maximum number in %s, %s and %s is :" %(a,b,c), end = ' ')
    if a > b:
        if a > c:
            print(a)
        else:
            print(c)
    else:
        if b > c:
            print(b)
        else:
            print(c)
'''
input_data = input("Enter 3 numbers to find out Maximum: \na,b,c: ")
[a,b,c]= input_data.split(',')
a,b,c = int(a),int(b),int(c)
max_of_three(a,b,c)
'''    

# Checking a Prime Number
from math import sqrt

def check_prime(number):
    # check if n=1 or n=0
    if number <= 1:
        return False
    # fact = number - 1
    # checking from (sq root of n) to 2
    fact = int(sqrt(number))    
    while fact > 1:
        if number % fact == 0:
            return False
        else:
            fact -= 1
    return True
'''
number = int(input("Enter a number to check prime: "))
if check_prime(number):
    print("%s is a Prime" %(number))
else:
    print("%s is not a Prime" %(number))
'''

# Find the nth number in Fibonacci_series
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
        
'''
print(fibonacci(34))
'''

# Printing a Fibonacci_series of first n numbers
def fibonacci_series(n):
    f1, f2 = 0, 1
    if n <= 0:
        return print("Please, enter a positve integer")
    elif n == 1:
        return print(f1)
    else:
        print("Fibonacci Sequence:",end=' ')
        index = 1
        f3 = 0
        while index <= n:
            print(f3, end =" ")
            f1 = f2
            f2 = f3
            f3 = f1 + f2
            index += 1


fibonacci_series(35)



    
        
    
    
    
        


