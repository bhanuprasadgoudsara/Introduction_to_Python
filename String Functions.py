name = "Sara Bhanu Prasad Goud"

print(name.count("a"))           #Returns the count of a given set of characters. Returns 0 if not found
'''5'''
print(name.replace("a","A"))     # Returns a new string by replacing a set of characters with another set of characters.
'''SArA BhAnu PrAsAd Goud'''
print(name)                      # It does not modify the original string
'''Sara Bhanu Prasad Goud'''
print(name.find("a"))            # Returns the first index position of a given set of characters
'''1'''
print(name.startswith("Sa"))     # Checks if a string starts with a specific set of characters, returns true or false accordingly.
'''True'''
print(name.endswith("ud"))       # Checks if a string ends with a specific set of characters, returns true or false accordingly.
'''True'''
print(name.isdigit())            # Checks if all the characters in the string are numbers, returns true or false accordingly.
'''False'''
print(name.upper())              # Converts the lowercase letters in string to uppercase
'''SARA BHANU PRASAD GOUD'''
print(name.lower())              # Converts the uppercase letters in string to lowercase
'''sara bhanu prasad goud'''
print(name.split("a"))           # Splits string according to delimiter and returns the list of substring.
                                 # Space is considered as the default delimiter.'''
['S', 'r', ' Bh', 'nu Pr', 's', 'd Goud']

print("")
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
