# The random module:
''' Python has many inbuilt packages and modules.
    One of the most useful modules is random.
    This module helps in generating random numbers'''

''' The code given below generates a random number between x and y-1 (both inclusive)
    using the randrange function of the random module.
    
Try out the below code and observe the output.'''
'''
import random
x, y = 10, 50
#help(random)
print(random.randrange(x,y))
'''
# The Math Module:
'''
math is another useful module in Python.
Once you have imported the math module, you can use some of the below functions:

Function            Explanation

math.ceil(x)        Smallest integer greater than or equal to x

math.floor(x)       Largest integer smaller than or equal to x

math.factorial(x)   Factorial of x

math.fabs(x)        Gives absolute value of x

Try out  the below code and observe the output. '''
'''
import math
num1=234.01
num2=6
num3=-27.01
print("The smallest integer greater than or equal to num1,",num1,":",math.ceil(num1))
print("The largest integer smaller than or equal to num1,",num1,":",math.floor(num1))
print("The factorial of num2,",num2,":", math.factorial(num2))
print("The absolute value of num3",num3,":",math.fabs(num3))
'''
'''
The smallest integer greater than or equal to num1, 234.01 : 235
The largest integer smaller than or equal to num1, 234.01 : 234
The factorial of num2, 6 : 720
The absolute value of num3 -27.01 : 27.01
'''

# Tryout the below code in python playground and observe the output. 
'''
boarding_call="Good Evening, this is the final call to AL passengers for the flight AL 466 which is planned to take off at 8.40A.M."
if(boarding_call.startswith("Good Evening")):
    print(boarding_call.replace("Good Evening","Good Morning"))
if(boarding_call.find("AL"))>=0:
    print("Welcome to Air Lines.")
if(boarding_call.endswith("A.M.")):
    print("Passengers are requested to have their breakfast.")
a=boarding_call.split(" ")
for i in a:
    if(i.isdigit()):
        print("Flight Number is specified to the passengers.")
print("Total number of times flight service name is specified in the boarding call:",boarding_call.count("AL"))
message="Thank you all..Have a nice journey!"
print(message.upper())
print(message.lower())
'''

crew_details={
    "Pilot":"Kumar",
    "Co-pilot":"Raghav",
    "Head-Strewardess":"Malini",
    "Stewardess":"Mala"
}
print("Before update:")
print("Co-pilot:",crew_details.get("Co-pilot"))
crew_details.update({"Flight Attendant":"Jane", "Co-pilot":"Henry"})
print("\nAfter update:")
print("Co-pilot:",crew_details.get("Co-pilot"))
print("Flight Attendant:",crew_details["Flight Attendant"])
 
