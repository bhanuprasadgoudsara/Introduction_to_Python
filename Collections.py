airlines = ["AL1","AL2","AL3"]
#print(airlines[-2],airlines[len(airlines)-2])
list2 = ['a','b','c','d','e','f','g','h','i']
print(list2.append('j'))
print(list2)
print(list2.index('f'))
print(list2)
print(list2.remove('e'))
print(list2)
print(list2.pop(3))
print(list2)
print(list2.insert(3,'e'))
print(list2)
print(list2.reverse())
print(list2)
print(list2.sort())
print(list2)
#print(list2[1:5],list2[-5:-1])

def check_adj_occurances(list1):
    count = 0
    for i in range(len(list1)-1):
        if list1[i] == list1[i+1]:
            count += 1
    return count
list_of_lists = [[1,1,5,100,-20,-20,6,0,0],[10,20,30,40,30,20],[1,2,2,3,4,4,4,10]]
for i in list_of_lists:
    print(check_adj_occurances(i))

'''
Sample Input

Sample Output

[1,1,5,100,-20,-20,6,0,0]

3

[10,20,30,40,30,20]

0

[1,2,2,3,4,4,4,10]

3
'''

# Tuple are immutable Elements can be homogeneous or heterogeneous i.e. read only
lunch_menu=("Welcome Drink","Veg Starter","Non-Veg Starter","Veg Main Course","Non-Veg Main Course","Dessert")
sample_tuple=("A",)
# lunch_menu[0]=""   # error

a, b = "Hello World", "AABGT6715H"
# strings re immutable
# a[3] = 'f' # error
'''
Write a Python program to generate the ticket numbers
for specified number of passengers traveling in a flight as per the details mentioned below:
The ticket number should be generated as airline:src:dest:number where

Consider AL1 as the value for airline

src and dest should be the first three characters of the source and destination cities.

number should be auto-generated starting from 101

The program should return the list of ticket numbers of last five passengers.
Note: If passenger count is less than 5, then return the list of all generated ticket numbers.
'''
# airlines = ["AL1","AL2","AL3"]
source_list = ['Hyderabad','Delhi','Goa']
destination_list = ['Bombay','Agra','Bali']
ticket_number = 100
def generate_ticket(airline,source,destination):
    global ticket_number
    ticket_number += 1
    return airline.upper() + ':' + source[:3].upper() + ':' + destination[:3].upper() + ':' + str(ticket_number)

def genearate_tickets(airlines,sourcelist,destinationlist):
    tickets = []
    for i in airlines:
        for j in sourcelist:
            for k in destinationlist:
                tickets.append(generate_ticket(i,j,k))
    if len(tickets) > 5:
        return tickets[-5:]
    else:
        return tickets
print(genearate_tickets(airlines,source_list,destination_list))

# Set:
# Creating a set: Removes the duplicates from the given group of values to create the set.
flight_set={500,520,600,345,520,634,600,500,200,200}
print(flight_set)
# Eliminating duplicates from a list : set function - removes the duplicates from the list and returns a set
passengers_list=["George", "Annie", "Jack", "Annie", "Henry", "Helen", "Maria", "George", "Jack", "Remo"]
unique_passengers=set(passengers_list)
print(passengers_list,"\n",unique_passengers)
a = {520,634,600,500,982,178,629,873,110}
b = {217,383,500,982,178,398,124,629,873,872,872,110,217,931}
print(a & b)
print(a | b)
print(b - a)

#dictionary
# Creating a dictionary
crew_details={ "Pilot":"Kumar","Co-pilot":"Raghav","Head-Strewardess":"Malini","Stewardess":"Mala" }
# Accessing the value using key
print(crew_details["Pilot"])
# Iterating through the dictionary : items() function gives both key and value, which can be used in a for loop.
for key,value in crew_details.items():
    print(key,":",value)
print("")
print("Before update:")
print("Co-pilot:",crew_details.get("Co-pilot"))
# Returns the value for given key. If the given key is not found, returns None

crew_details.update({"Flight Attendant":"Jane", "Co-pilot":"Henry"})
print("\nAfter update:")
print("Co-pilot:",crew_details.get("Co-pilot"))
print("Flight Attendant:",crew_details["Flight Attendant"])
# Updates the dictionary with the given key-value pairs.
# If a key-value pair is already existing, it will be overwritten,
# otherwise it will be added to the dictionary

                    

