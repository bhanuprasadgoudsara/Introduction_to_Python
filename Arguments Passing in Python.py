'''
In programming, there are two ways in which arguments can be passed to functions: 
    1.pass by value 
    2.pass by reference

Some languages use pass by value by default while others use pass by reference.
Some languages support both and allow you to choose.

In Python, we don't have to think about pass by value and pass by reference as it does that automatically for you.
To emulate this using Python, we use the concept of mutability.
'''
#Pass by value method : If the argument passed is immutable then it follows pass by value.
# Note: Till now we have seen int, float, string data types which are immutable.
def change_val(arg):
    arg += 20
    print("In function, num =",arg)

num = 10
print('Before function call, num =',num)
change_val(num)
print('After function call, num =',num)

'''
Before function call, num = 10
In function, num = 30
After function call, num = 10
'''

#Pass by reference method: if the argument passed is mutable then it follows pass by reference.
def change_vals(arg):
    arg += [20]
    print('In function, num =',arg)

num1 = [10]
print('Before function call, num =',num1)
change_vals(num1)
print('After function call, num =',num1)

'''
Before function call, num = [10]
In function, num = [10, 20]
After function call, num = [10, 20]
'''

    
