# Built-in Exception in Python
''' Python has many kinds of exceptions predefined as part of the language.
    Here are some of the common types.'''



# ZeroDivisionError
''' When a value is divided by zero'''
try:
    num_list=[]
    total=0
    avg=total/len(num_list)
except ZeroDivisionError:
    print("Zero diviion Error")
    
# TypeError
''' When we try to do an operation with incompatible data types'''
try:
    total=10
    total+="20"
except TypeError:
    print("Incompatible Data Type Error")
    
# NameError
''' When we try to access a variable which is not defined'''
try:
    avg=total1/10 # where total1 is not defined
except NameError:
    print("Variable name is not defined")

    
# IndexError
''' When we try to access an index value which is out of range'''
try:
    num_list=[1,2,3,4]
    value=num_list[4]
except IndexError:
    print("Index out of range")

    
# ValueError
''' When we use a valid data type for an argument of a built-in function but passes an invalid value for it'''
#string is a valid data type for int() but the value “A” is invalid, as "A" can't be converted into int.
try:
    value="A"
    num=int(value)
except ValueError:
    print("Invalid Type Converion")


''' Python also allows us to handle different exceptions that can occur separately.
    That means you can have a different action or message for every unique exception that occurs.'''

def calculate_expenditure(list_of_expenditure):
    total=0
    try:
        for expenditure in list_of_expenditure:
            total+=expenditure
        print("Total:",total)
        avg=total/num_values
        print("Average:",avg)
    except ZeroDivisionError:
        print("Division by Zero error")
    except TypeError:
        print("Wrong data type")
    except:
        print("Some error occured")
list_of_values=[100,200,300,"400",500]
num_values=0
calculate_expenditure(list_of_values)


# Note:
''' 1.Default except block is the one without any type mentioned.

    2.If an error occurs and the matching except block is found, then that is executed.

    3.If an error occurs and the matching except block is not found, it executes the default except block.

    4.If an error occurs and the matching except block is not found
      and if the default except block is also not found, the code crashes.

    5.The default except block, if present should be the last except block,
      otherwise it will result in a runtime error.'''

''' If an exception occurs inside a function and
    if the exception is not caught inside it,
    then the exception is transferred to the function call.
    We have another opportunity to catch it, if we write function call inside another try and except block.'''

def calculate_sum(list_of_expenditure):
    total=0
    try:
        for expenditure in list_of_expenditure:
            total+=expenditure
        print("Total:",total)
        avg=total/no_values
        print("Average:",avg)
    except ZeroDivisionError:
        print("Divide by Zero error")
    except TypeError:
        print("Wrong data Type")

try:
    list_of_values=[100,200,300,400,500]
    num_values=len(list_of_values)
    calculate_sum(list_of_values)
except NameError:
    print("Name error occured")
except:
    print("Some error occured")
    
