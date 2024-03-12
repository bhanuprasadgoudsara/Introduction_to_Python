# Exception handling in python:
''' Sometimes the programs may misbehave or terminate/crash unexpectedly
    due to some unexpected events during the execution of a program.

    These unexpected events are called as EXCEPTIONS and

    the process of handling them to avoid misbehavior or crashing the program is called as EXCEPTION HANDLING.'''

'''
def calculate_expenditure(list_of_expenditure):
    total=0
    for expenditure in list_of_expenditure:
        total+=expenditure
    print(total)
list_of_values=[100,200,300,"400",500]
calculate_expenditure(list_of_values)
'''

# TypeError: unsupported operand type(s) for +=: 'int' and 'str'

'''  If we add a condition to check whether the expenditure is of type int, that would solve this error.'''
'''
def calculate_expenditure(list_of_expenditure):
    total=0
    for expenditure in list_of_expenditure:
        if(type(expenditure) is int):
            total+=expenditure
        else:
            print("Wrong data type")
            break
    print(total)
list_of_values=[100,200,300,"400",500]
calculate_expenditure(list_of_values)
'''
'''
Wrong data type
600
'''
''' Although we have handled this error using if statement,
    the function itself returns wrong output when there is error in the input.
    
    The ideal situation would be if the function can tell us that something went wrong.
    
    In python we can create a try and except block of code to handle exceptions.
    If any exception occurs in the try block of code, it will jump to except block of code.
    Once the except block is executed, the code continues to execute other statements outside except block.
    
    With this we will not get incorrect output like before.'''

def calculate_expenditure(list_of_expenditure):
    total=0
    try:
        for expenditure in list_of_expenditure:
            total+=expenditure
        print(total)
    except:
        print("Some error occured")
    print("Returning back from function.")
list_of_values=[100,200,300,"400",500]
calculate_expenditure(list_of_values)
'''
Some error occured
Returning back from function.
'''

    

    
