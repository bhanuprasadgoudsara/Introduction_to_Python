# File Handling in Python:
''' File can be accesed from a python program for
    - reading the data from a file and
    - writing the data into a file'''

# Opening a file in Python:
'''  Python provides a funcion called open() to open a file programmatically.
    open() function returns a file object
    this file object used for other file operations like reading, writing and closing of the file'''

# Syntax: file_object = open(file_name_path[,access_mode])

''' where,
        - file_name_path:
            it is the file name or path of the file to be opened.
        - access_mode:
            mode with which the file has to be opened which is optional.
            if not specified, default value will be read.
        - file_object:
            it is the object returned by open method which is used for further operations'''

# Access mode:

# 1. r:     READ MODE
''' opened read mode, if the file exists
    otherwise, throws an error,  if the file does not exists'''

# 2. w:     WRITE MODE
''' if the file exists, thencontent present in the file is truncated
    otherwise if the file does not exists, it will create a new file and open it for writing '''

# 3. a:     APPEND MODE
''' if the file exists, then content present in the file is preerved
    otherwise if the file does not exists, it will create a new file and open it for appending '''

""" Eg: fhr = open("data.txt","r") """


# Closing a File:
''' The number of files that can be simultaneously opened by a program is limited.
    So it is very important to close all the files,
    once the operations are completed.  '''

# Syntax: file_object.close()
"""Eg: fhr.close()  """

# Reading from a file
''' Consider a file data.txt with below data

    "this is first line
    you are reading the second line
    now you are dealing with third line" '''

# Reading Single Line:
''' Python provides readline() function to read the single line from a file at a time.
    When the end of the file is reached, it returns an empty string.'''

# Syntax : var_name = file_object.readline()

'''
Example:

fhr=open("data.txt","r")
line1=fhr.readline()    
print(line1,end="")
line2=fhr.readline()    
print(line2,end="")
line3=fhr.readline()    
print(line3,end="")

Output:

this is first line
you are reading the second line
now you are dealing with third line
'''

# Reading the contents of a file into a list:
''' Python provides readlines() function to read entire content of file into a variable
    where eachline will present as an element of the list '''

# Syntax : var = file_object.readlines()

'''
fhr=open("data.txt","r")
list_var=fhr.readlines()
#print(list_var)
for line in list_var:
    print(line,end="") 
fhr.close()

Output:

this is first line
you are reading the second line
now you are dealing with third line
'''
# Reading the contents of a file into a string:
''' Python provides read(size) function
    to read the specified size(number) of charecters
    from the file as a string into a variable.
    if no size is specified,
    the entire content of the file is read as a string into a variable.'''

# Syntax : var_name = file_name.read(size)

# Example 1:
'''
fhr=open("data.txt","r")
data =fhr.read(10)
print(data)
fhr.close()

Output:

this is fi
'''
# Example 2:
'''
fhr=open("data.txt","r")
data =fhr.read()
print(data)
fhr.close()

Output:

this is first line
you are reading the second line
now you are dealing with third line
'''

# Iterating through file object read the content line by line:
''' We can also iterate through file object to read content of the file line by line in a simple way.
    THis method is fast and efficient campared to other methods of reading the file contents.'''

'''
Example 

fhr = open("data.txt","r")
print(fhr)
for line in fhr:
    print(line,end ='')
fhr.close()
'''
# Writing into file
''' Python provides write(data) function to write the given data which is a string into the file.
    and it returns the number of charecters written into file.'''

# Syntax: var = file_object.write(data)
''' where,
 - data is the content which is a string to be written into a file
 - var is a variable assigned with number characters written into the file.'''

'''
Example:

fhr = open("data.txt","r")
data = fhr.read()
print("Before writing:")
print(data)
fhr.close()

fhw = open("data.txt","w")
num = fhw.write("this new first line written\n")
num1 = fhw.write("this new second line written\n")
print("num:",num)
print("num1:",num1)
fhw.close()

fhr = open("data.txt","r")
data = fhr.read()
print("After writing:")
print(data)
fhr.close()

Output:

Before writing:
this is first line
you are reading the second line
now you are dealing with third line
num: 28
num1: 29

After writing:
this new first line written
this new second line written

Note:
The file ‘data.txt’ is opened in write mode,
so previous content of file is truncated
and it contains only two lines after writing into it.
'''


"""
Another example:

fhr=open("data.txt","r")
data =fhr.read()
print("Before writing:")
print(data)
fhr.close()
fhw=open("data.txt","a")
num=fhw.write("this new first line written\n")
num1=fhw.write("this new second line written\n")
print("num:",num)
print("num1:",num1)
fhw.close()
fhr=open("data.txt","r")
data =fhr.read()
print("After writing:")
print(data)
fhr.close()

Output:

Before writing:
this is first line
you are reading the second line
now you are dealing with third line
num: 28
num1: 29
After writing:
this is first line
you are reading the second line
now you are dealing with third line
this new first line written
this new second line written

Note: The file 'data.txt' is opened in append mode,
so the previous content of file is preserved
and it contains all five lines after writing into it.
"""

# Getting current position of the file object pointer:
''' Python provides tell() method to get current position which is pointed by file object within the file.'''

# Syntax : file_object.tell()

'''
Example:

fhr = open("data.txt","r")
cur_pos = fhr.tell()
print(cur_pos)
data = fhr.readline()
print(data)

cur_pos = fhr.tell()
print(cur_pos)
data = fhr.readline()
print(data)
fhr.close()

Output:

0
this new first line written

20
this new second line written
'''

# Navigating the file object pointer
''' Python provides seek() function to navigate the file object pointer to the required position specified'''
# Syntax : file_object.seek(offset,[whence])
'''
where,
    - file_object indicates the file object pointer to be navigated
    - offset indicates which position the file object pointer is to be navigated
        if offset is,
        - positive, navigation is done in forward direction
        - negative, naviagation is done in backward direction.'''

'''  If whence value is
    - 0, navigation will take the reference of the beginning of the file(absolute positioning)
    - 1, navigation will take the reference of current position (relative positioning)
    - 2, navigation will take the reference of end of file(relative positioning)'''

# Note:
''' If you are working with is a text file, then the access mode of the file should be 'rb+'
    (which opens a file for reading and writing in binary format)
    other wise, relative positioning will misbehave'''

'''
Example:

fhr=open("data.txt","rb+")
print(fhr.tell())
fhr.seek(12) #navigates to 12th position from beginning of the file
print(fhr.tell())
fhr.seek(3,1) #navigates to 3rd position from current position of the file object position
print(fhr.tell())
fhr.seek(-3,2)#navigates to 3rd position from end of the file in backward direction
print(fhr.tell())
fhr.close()

Output:

0
12
15
56
'''

# File Object attributes:

# file_object.cloed : closed attributes returns true if the file is closed else returns false.

# file_object.mode : mode attribute returns mode in which the file has been opened.

# file_object.name : name attribute returns the name of the file opened.

'''
Example:

fhr = open("data.txt","rb+")
print("file name:",fhr.name)
print("access mode:",fhr.mode)
print("cloed?",fhr.closed)
fhr.close()
print("after closing the file closed?",fhr.closed)

Output:

file name: data.txt
access mode: rb+
closed? False
after closing the file closed? True'''

