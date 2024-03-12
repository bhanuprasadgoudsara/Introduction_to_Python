#1
''' Given a list of numbers, write a Python function to return the list of prime numbers present in it.

    Example: input:[7,9,11,13,15,20,23] output:[7,11,13,23]'''

def return_prime(list1):
    maximum = max(list1)
    new_list = []
    print(maximum)
    for i in range (len(list1)):
        for j in range(2,list1[i]):
            if list1[i] % j == 0:
                new_list.append(list1[i])
                break
    for i in range(len(new_list)):
        list1.remove(new_list[i])
    return list1
    
# print(return_prime([7,9,11,13,15,20,23]))

#2
''' Write a python function find_common_characters(msg1,msg2) to display
    all the common characters between given two strings.
    Return -1 if there are no matching characters.

    Note: Ignore blank spaces if there are any. Perform case sensitive string comparison wherever necessary.

    Example: msg1="I like Python", msg2="Java is a very popular language" output=lieyon'''

def find_common_characters(msg1,msg2):
    common = ''
    for i in msg1:
        if i in msg2 and i != ' ':
            common = common + i
    if common == '':
        return -1
    else:
        return common

msg1="I like Python"
msg2="Java is a very popular language"

# print(find_common_characters(msg1,msg2))
            
#3
''' Write a python function, find_pairs_of_numbers(num_list,n)
    which accepts a list of positive integers with no repetitions
    and returns count of pairs of numbers in the list that adds up to n.
    The function should return 0, if no such pairs are found in the list.

    Example: num_list=[1, 2, 7, 4, 5, 6, 0, 3], n=6 output:3

    num_list= [3, 4, 1, 8, 5, 9, 0, 6], n=9 output:4'''

def find_pairs_of_numbers(num_list,n):
    count_of_pairs = 0
    for i in range(len(num_list)):
        for j in range(i,len(num_list)):
            if i != j and num_list[i]+num_list[j] == n:
                count_of_pairs += 1
    return count_of_pairs

num_list1=[1, 2, 7, 4, 5, 6, 0, 3]
num_list2= [3, 4, 1, 8, 5, 9, 0, 6]
n1, n2 = 6, 9
#print(find_pairs_of_numbers(num_list1,n1))
#print(find_pairs_of_numbers(num_list2,n2))

#4
''' The python function, find_average() given below,
    is written to accept a list of marks and return the average marks.
    On execution, the program is resulting in an error.'''

def find_average(mark_list):
          total=0
          for i in range(0, len(mark_list)):
                   total+=mark_list[i]
          marks_avg=total/len(mark_list)
          return marks_avg
m_list=[1,2,3,4]
# print("Average marks:", find_average(m_list))


'''
1: Add code to handle the exception occurring in the code.

2: Make the necessary correction in the program to remove the error.

3: Make the following changes in the code, execute, observe the results. Add code to handle the errors occurring in each case.
'''
print("#4")
try:
    total=0
    for i in range(0, len(mark_list)):
        total+=mark_list1[i]
        marks_avg=total/len(mark_list)
    print("Average marks:", marks_avg)
except NameError:
    print("Variable name is not defined")
except:
    print("Some Error Occurred")   
'''
Case – 1: Initialize m_list as ["1",2,3,4]
'''
print("")
print("Case - 1:")
try:
    m_list=["1",2,3,4]
    print("Average marks:", find_average(m_list))
except ZeroDivisionError:
    print("Zero Division Error")
except TypeError:
    print("Operation Incompatible Data Type Error")
except ValueError:
    print("Invalid Type Converion")
except NameError:
    print("Variable name is not defined")
except IndexError:
    print("Index out of range")
except:
    print("Some Error Occurred")
finally:
    print("Code Execution Complete")
'''
Case – 2: Initialize m_list as given below
mark1="A"
mark1=int("A")
m_list=[mark1,2,3,4]
'''
print("")
print("Case - 2:")
try:
    mark1="A"
    mark1=int("A")
    m_list=[mark1,2,3,4]
    print("Average marks:", find_average(m_list))
except ZeroDivisionError:
    print("Zero Division Error")
except TypeError:
    print("Operation Incompatible Data Type Error")
except ValueError:
    print("Invalid Type Converion")
except NameError:
    print("Variable name is not defined")
except IndexError:
    print("Index out of range")
except:
    print("Some Error Occurred")
finally:
    print("Code Execution Complete")


    
'''
Case – 3: Initialize m_list as []
'''
print("")
print("Case - 3:")
try:
    mark1="A"
    mark1=int("A")
    m_list=[mark1,2,3,4]
    print("Average marks:", find_average(m_list))
except ZeroDivisionError:
    print("Zero Division Error")
except TypeError:
    print("Operation Incompatible Data Type Error")
except ValueError:
    print("Invalid Type Converion")
except NameError:
    print("Variable name is not defined")
except IndexError:
    print("Index out of range")
except:
    print("Some Error Occurred")
finally:
    print("Code Execution Complete")


'''
Case – 4: Make the following change in the for loop statement


for i in range(0, len(mark_list)+1):
'''
print("")
print("Case - 4:")
try:
    total=0
    mark_list = [1,2,3,4]
    #for i in range(0, len(mark_list)):
    for i in range(0, len(mark_list)+1):
        total += mark_list[i]
        marks_avg = total/len(mark_list)
    print("Average marks:", marks_avg)
except ZeroDivisionError:
    print("Zero Division Error")
except TypeError:
    print("Operation Incompatible Data Type Error")
except ValueError:
    print("Invalid Type Converion")
except NameError:
    print("Variable name is not defined")
except IndexError:
    print("Index out of range")
except:
    print("Some Error Occurred")
finally:
    print("Code Execution Complete")



"""
4#
Variable name is not defined

Case - 1:
Operation Incompatible Data Type Error
Code Execution Complete

Case - 2:
Invalid Type Converion
Code Execution Complete

Case - 3:
Invalid Type Converion
Code Execution Complete

Case - 4:
Index out of range
Code Execution Complete
"""
