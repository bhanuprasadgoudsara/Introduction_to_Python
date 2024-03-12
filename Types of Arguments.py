'''
Programming languages allow controlling the ordering and default values of arguments.
In Python, we will observe the following:
'''
# Positional:
def func_positional(arg1,arg2):
    result = arg1 + arg2
    return result
val1, val2 = 2, 3
res = func_positional(val1,val2)
print(res)
''' Defult way of specifying arguments.
    In this, the order, count and type of actual arguments should exactly match that of the formal arguments.
    Else, it will result in error '''

# Keywords:
def func_keyword(arg1,arg2):
    result = arg1 - arg2
    return result
val3, val4 = 19, 9
res1 = func_keyword(arg2=val3,arg1=val4)
print(res1)
''' Allows flexibility in the order of passing the actual arguments by mentioning the argument name'''

# Default:
def func_default(arg1,arg2=5): # here 5 is a default value
    result = arg2 - arg1
    return result
val5 = 27
res2 = func_default(val5)
print(res2)
''' Allows to specify a default value for an argument in the function signature.
    It is used only when no value is passed for that argument, else it works normally.
    In Python, default arguments should be last in the order '''

# variable argument count:
def func_vari_arg_count(arg1,arg2,*arg3):
    result = [arg1,arg2]
    for i in arg3:
        result.append(i)
    return result

print(func_vari_arg_count(3,4,5,6,7))
''' Allows a functin to have variable number of arguments.
    In Python, any argument name starting with '*' is considered to be a varying length argument.
    It should be last in the order.
    It works by copying all the values beyond that position into a tuple'''

