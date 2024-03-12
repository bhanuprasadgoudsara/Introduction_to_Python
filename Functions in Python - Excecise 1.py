# Problem - 1:
''' Write a Python function factorial(num) which returns the factorial of a given number.'''
'''
def factorial(num):
    # Iteration :
    
    if num <= 1:
        return 1
    factorial = 1
    while num > 1:
        factorial *= num
        num -= 1
    return factorial
    
    # Recursion :
    
    if num == 0:
        return 1
    elif num == 1:
        return 1
    else:
        return (num * factorial( num - 1 ))
    

print(factorial(6))
'''   
        

# Problem - 2:
''' Write a Python Function is_palindrome(num) that accepts an integer num as argument
    and returns True if the num is palindrome else returns false.
    Invoke the function and based on return value print the output.
    
    Example: num=12321 output: Given number is a palindrome, num=12345 output: Given number is not a palindrome'''

def is_palindrome(number):
    '''
    # comparing first and last digits simultaneously
    n = len(str(number)) - 1
    # m = 0
    while number > 0:
        # m += 1 ; print(m)
        first_digit = ( number // pow(10,n) )
        last_digit = ( number % 10 )
        if first_digit == last_digit:
            number = ( number - ( first_digit* (pow(10,(n)))) ) // 10
            n -= 2
        else:
            return False
    return True
    '''
    '''
    # reversing and storing in an another number
    temp = number
    rev = 0
    # m = 0
    while (number > 0):
        # m += 1 ; print(m)
        digit = number % 10
        rev = rev*10 + digit
        number = number // 10
    if (temp == rev):
        return True
    else:
        return False
    

number = int(input("Enter a number to check Palindrome : "))

if is_palindrome(number):
    print("%s is a Palindrome" %number)
else:
    print("%s is not a Palindrome" %number)

'''

# Problem - 3:
''' Write a Python function check_amicable_numbers(num1, num2) that accepts two numbers num1 and num2 as arguments
    and returns True if the given pair of numbers are amicable numbers else return false.
    Invoke the function and based on return value print the numbers are amicable numbers or not.

    num1 and num2 are said to be amicable numbers
    if sum of all the proper devisors (except num1 itself) of num1 is equal to num2
    and sum of all the proper devisors of num2 (except num1 itself) is equal to num1.

    Example: 220 and 284 are amicable numbers as
    Proper devisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110 whose sum is 284
    Proper devisors of 284 are 1, 2, 4, 71, 142 whose sum is 220 '''
'''
def check_amicable_numbers(num1, num2):
    temp1 = num1 - 1
    temp2 = num2 - 1
    sum1 = 0
    sum2 = 0
    m = 0
    while temp1 > 0:
        m += 1 
        if num1 % temp1 == 0:
            sum1 += temp1
        temp1 -= 1
    while temp2 > 0:
        m += 1
        
        if num2 % temp2 == 0:
            sum2 += temp2
        temp2 -= 1
        
        if temp2 == num1:
            temp2 -= 1
            continue
        else:
            if num2 % temp2 == 0:
                sum2 += temp2
            temp2 -= 1
        
    print(m)
    if sum1 == num2 and sum2 == num1:
        return True
    else:
        return False
print(check_amicable_numbers(220,284))
'''

# Problem - 4:
''' Write a Python function right_shift(num, n) that takes two numbers num and n as  arguments
    and returns value of the integer num rotated to the right by n positions.
    Assume both the numbers are unsigned.
    Invoke the function and print the return value.

    Hint: use >> binary operator to shift the bits.
    Example: num=60, n=2 result=15  '''
'''
def right_shift(num,n):
    result = num >> n
    return print(result)

right_shift(60,2)
'''


# Problem - 5:
''' Write a Python function check_strong_number(num) that accepts a positive integer as argument
    and returns True if the number is strong number else false.
    Invoke the function and based on return value print the number is strong number or not.

    A number is said to be strong number, if the sum of factorial of each digit of the number is equal to the given number.

    Example:145 is strong number as
    1!=1
    4!=24
    5!=120
    Sum of all these is 145 '''
'''
def check_strong_number(num):
    temp = num
    sum1 = 0
    while num > 0:
        digit = num % 10
        num = num // 10
        factorial = 1
        while digit > 0:
            factorial *= digit
            digit -= 1
        sum1 += factorial
        print(f"Factorial: %-5d, Sum: {sum1}"%factorial)
    if temp == sum1:
        return True
    else:
        return False
        
num = 145
if check_strong_number(num):
    print("%s is a strong number" %num)
else:
    print("%s is not a strong number" %num)
'''
