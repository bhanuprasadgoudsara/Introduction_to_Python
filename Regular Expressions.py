# Regular Expression:
''' Many times a lot of data would be sorted in files and we may have to pick and change only relevent portions from a file.

    Even though there are string functions which allows us to manupulate strings, when dealing with more complicated requirements,

    we would need more powerful tools.'''

''' Regular Expressions are used to check and extract relevent portions of a string based on a pattern and modify if required.

    Python has a module named "re" for regular expressions.'''

# Working with 're' module:
''' Two commonly used methods in the "re" module are "search" and "sub".
    Search is used to find a pattern and
    Sub is used to perform a substitution.'''
'''
re -- > Module Name
search -- > Method Name
Airlines -- > Expression
Input_Data -- > Target string
'''

# Example 0:

import re

Input_Data = "Flight Savana Airlines a2134"

regex = re.search( r"Airlines", Input_Data )

print(regex)

# Output 0 : <re.Match object; span=(14, 22), match='Airlines'>



# Example 1:

print(" 1: ",re.search(r"Air","Airline"))

# Output 1:  <re.Match object; span=(0, 3), match='Air'>



# Example 2:

print(" 2: ",re.search(r"Air","airline"))

# Output 2:  None


    
''' Here, r in front of the search pattern indicates 'raw string' where the special characters are treated as normal characters.
    The output will be 'None' if the pattern is not found.

    If you want to search the pattern "Air" in the given string "Airline" here are few example for that.'''

# Example 3: '.' Used to match one occurrence of any character

print(" 3: ",re.search(r"A..l","Aopline"))

# Output 3:  <re.Match object; span=(0, 4), match='Aopl'>



# Example 4: '\d' Used to match one occurrence of any digit from 0-9

print(" 4: ",re.search(r"A\dl","A2line"))

# Output 4:  <re.Match object; span=(0, 3), match='A2l'>



# Example 5: '*' Used to match zero or more occurrences of previous character

print(" 5: ",re.search(r"A\d*","A234line"))

# Output 5:  <re.Match object; span=(0, 5), match='A2234'>



# Example 6: '+' Used to match one or more occurrences of previous character

print(" 6: ",re.search(r"A\d+","Airline"))

# Output 6:  None



# Example 7: '?' Used to match zero or one occurrence of previous character

print(" 7: ",re.search(r"A\d?i","Airline"))

# Output 7:  <re.Match object; span=(0, 2), match='Ai'>



# Example 8: {n} Used to match exactly n occurrences of previous character

print(" 8: ",re.search(r"A\d{3}i","A223irline"))

# Output 8:  <re.Match object; span=(0, 5), match='A223i'>



# Example 9: [] Used to match one occurrence of any characters present within square brackets

print(" 9: ",re.search(r"A[4-8]l","A2line"))

# Output 9:  None



# Example 10: '^' Used to match a pattern at the beginning of a string

print(" 10: ",re.search(r"^A","Airline"))

# Output 10:  <re.Match object; span=(0, 1), match='A'>



# Example 11: '$' Used to match a pattern at the end of a string

print(" 11: ",re.search(r"e$","Airline"))

# Output 11:  <re.Match object; span=(6, 7), match='e'>



# Example 12: '\w' Used to match an word character which includes alphabets(a-zA-Z), digits(0-9) and '_'

print(" 12: ",re.search(r"\w$","Airline%"))

# Output 12:  None



# Example 13: '\s' Used to match single space or sequence of spaces (including \t \n)

print(" 13: ",re.search(r"Air\s","Airline"))

# Output 13:  None



# Example 14: '|' Used to match any one pattern which is on either side of it

print(" 14: ",re.search(r"Hell|Fell","Fellow"))

# Output 14:  <re.Match object; span=(0, 4), match='Fell'>



# re - Replacing data
'''
We can use the function ‘sub’ to perform a substitution.
Go through the below example
'''

flight_details = "Flight Savana Airlines a2134"
print(flight_details)
# Output : Flight Savana Airlines a2134

print(re.sub(r"Flight",r"Plane",flight_details))
# Output : Plane Savana Airlines a2134

# QUIZ:

'''
song="JINGLE Bells jingle Bells Jingle All The Way"
print(song)
song.upper()
print(song)
song_words=song.split()
count=0
for word in song_words:
    if(word.startswith("jingle")):
        count=count+1
print(count)

sample_dict={'a':1,'b':2}
print(sample_dict)
sample_dict.update({'b':5, 'c':10 })
print(sample_dict)
print(sample_dict.get('a'),sample_dict.get('b'),sample_dict.get('c'))

import math
num_list=[100.5,30.465,-1.22,20.15]
print(num_list)
num_list.insert(1, -100.5)
print(num_list)
num_list.pop(0)
print(num_list)
num_list.sort()
print(num_list)
print((num_list[0]))
print(math.fabs(num_list[0]))
print(math.ceil(math.fabs(num_list[0])))
 
'''
