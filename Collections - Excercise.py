# PROBLEM 1:
''' Write a Python function proper_divisors(num) which
    returns a list of all the proper divisors of given number.
    Example: Proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110'''

'''
def proper_divisors(num):
    list1 = []
    temp = 1
    while temp < num:
        if num % temp == 0:
            list1.append(temp)
        temp += 1
    return list1
print(proper_divisors(220))
'''

# PROBLEM 2:
''' Write a Python function generate_fibanacci(n) to return a list of first n Fibonacci numbers.'''



# PROBLEM 3:
''' Write a Python program to generate the next 15 leap years starting from a given year.
    Populate the leap years into a list and display the list.'''

'''
def gen_next_15_leap_years(year):
    years = []
    while len(years) < 15:
        if year % 4 == 0 and ( year % 100 != 0 or year % 400 == 0 ):
            years.append(year)
        year += 1
    return years

print(gen_next_15_leap_years(1890))
'''


# PROBLEM 4:
''' Given a string containing uppercase characters (A-Z),
    compress the string using Run Length encoding.
    Repetition of character has to be replaced by storing the length of that run.
    Write a python function encode(message)  which performs the run length encoding for
    a given String and returns the run length encoded String.
    Provide different String values and test your program.
    Example: message=AAAABBBBCCCCCCCC  output: 4A4B8C'''
'''
def encode(message):
    letters = []
    new_msg = ' '
    for i in message:
        letters.append(i)
    letters = list(set(letters))
    letters.sort()
    for i in range(len(letters)):
        count = message.count(letters[i])
        new_msg = new_msg + str(count) + letters[i] 
    return new_msg[1:]
        
print(encode('AAAABBBBCCCCCCCC'))
#  output: 4A4B8C
'''


# PROBLEM 5:
''' Represent a small bilingual (English-Swedish) glossary given below as a Python dictionary
    {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"} 
    and use it to translate your Christmas wishes from English into Swedish.
    That is, write a Python function translate(b_dict,list_words) that accepts the bilingual dictionary
    and a list of English words (your Christmas wish) and returns a list of equivalent Swedish words.'''

'''
def translate_english_to_swedish(b_dict,list_words):
    list_words = list_words.lower()
    print(list_words)
    list_words = list_words.split(' ')
    swedish_mean = ' '
    for i in list_words:
        swedish_mean = swedish_mean + b_dict[i] + ' '
    return swedish_mean[1:]
        
#bilingual_English_Swedish_glossary
trans_b_dict = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}
list_words = "Merry Christmas and Happy new year"

print(translate_english_to_swedish(trans_b_dict,list_words))
'''


