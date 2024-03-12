# PROBLEM 1:
''' Write a python function, encrypt_sentence(msg) which accepts a message
    and encrypts it based on rules given below and returns the encrypted message.

    Words at odd position -> Reverse It
    Words at even position -> Rearrange the characters so that all consonants appear
                              before the vowels and their order should not change

    Note: Assume that the sentence would begin with a word and there will be only a single space between the words.

          Perform case sensitive string operations wherever necessary.

    Example: msg=the sun rises in the east    output=eht snu sesir ni eht stea'''
                                        
import re
def encrypt_sentence(msg):
    msg_words_list = msg.split(" ")
    # print(msg_words_list)
    encrypted_msg = ''
    for i in range(len(msg_words_list)):
        if i%2 != 0:
            vow_words = ''
            con_words = ''
            for j in range(len(msg_words_list[i])):
                # print(j,re.search(r"[a,A,e,E,i,I,o,O,u,U]",msg_words_list[i][j]))
                if msg_words_list[i][j] in ['a','A','e','E','i','I','o','O','u','U']:
                # if re.search(r"[a,A,e,E,i,I,o,O,u,U]",msg_words_list[i][j]
                    vow_words = vow_words + msg_words_list[i][j]
                else:
                    con_words = con_words + msg_words_list[i][j]
            encrypted_msg = encrypted_msg + con_words + vow_words + ' '
            # print(encrypted_msg)
        else:
            odd_word = ''
            for j in range((len(msg_words_list[i])-1),-1,-1):
                odd_word = odd_word + msg_words_list[i][j]
            encrypted_msg = encrypted_msg + odd_word + ' '
            # print(encrypted_msg)               
    return encrypted_msg

# print(encrypt_sentence("the sun rises in the east"))




# PROBLEM 2:
''' Write a Python program to find the number of characters present the given string.'''

def len_string(string):
    #return len(string)  #total char including spaces
    str1 = string.replace(' ','')
    print(str1)
    return len(str1)
# print(len_string("the sun rises in the east"))




# PROBLEM 3:
''' Write a Python program to find the numbers of words present in the given sentence.'''

def num_of_words(sentence):
    word_list = sentence.split(' ')
    return len(word_list)
#print(num_of_words("the sun rises in the east"))


 
# PROBLEM 4:
''' Write a Python function words_count(sentence) to return a dictionary with
    the length of words as key and number words with such length as value.

    Example: sentence=“I love python and it so easy to learn” sample output={1:1,4:2,5:1,3:1,2:3,6:1}'''
def words_count(sentence):
    word_list = sentence.split(' ')
    list1 = []
    dict1 = {}
    for i in range(len(word_list)):
        list1.append(len(word_list[i]))
    #print(list1)
    list2 = list(set(list1))
    for i in list2:
        dict1.update({i:list1.count(i)})
    '''
    for i in list2:
        dict1.update({str(i):0})
    for key,value in dict1.items():
        for i in range(len(word_list)):
            if int(key) == len(word_list[i]):
                dict1[key] += 1
    '''
    return dict1

#print(words_count('I love python and it so easy to learn'))

# PROBLEM 5:
''' Write a Python function vowel_count(sentence) to return a dictionary
    with vowels, consonants, others as key and respective number of vowels, consonants, others characters as value.

    Note: Do case insensitive operations

    Example: sentence=“I love python and it so easy to learn”

                 sample output={“vowels”:12,”consonants”:17, “others”:8}'''

import string
alphabets = string.ascii_uppercase
def vowel_count(sentence):
    dict1 = {'vowels':0,'consonants':0, 'others':0}
    for i in sentence:
        if i.upper() in alphabets:
            if i.upper() in 'AEIOU':
                dict1['vowels'] += 1
            else:
                dict1['consonants'] += 1
        else:
            dict1['others'] += 1
            
        '''
        if i.upper() in 'AEIOU':
            dict1['vowels'] += 1
        elif i.upper() in 'BCDFGHJKLMNPQRSTVWXYZ':
            dict1['consonants'] += 1
        else:
            dict1['others'] += 1
        '''
    return dict1

print(vowel_count('I love python and it so easy to learn'))
