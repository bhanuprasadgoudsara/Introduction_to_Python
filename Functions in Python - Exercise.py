def find_square(number):
    return number * number

print(find_square(12))

def find_sum(n):
    return ((n*(n+1))/2)

print(find_sum(9))

# Types of Arguments:
'''
def display1(flight_number, seating_capacity):
    print("Flight Number:", flight_number)
    print("Seating Capacity:", seating_capacity)
print("code-1: positional arguments")
display1("FN789",200)
#Uncomment and execute the below function call statement and observe the output
display1(300,"FN123")
def display2(flight_number, seating_capacity):
    print("Flight Number:", flight_number)
    print("Seating Capacity:", seating_capacity)
print("-------------------------------------------------")
print("code-2: keyword arguments")
display2(seating_capacity=250, flight_number="FN789")
def display3(flight_number, flight_make="Boeing", seating_capacity=150):
    print("Flight Number:", flight_number)
    print("Flight Make:", flight_make)
    print("Seating Capacity:", seating_capacity)
print("-------------------------------------------------")
print("code-3: default arguments")
display3("FN789","Eagle")
#Uncomment and execute the below function call statements one by one and observe the output
display3("FN234")
display3("FN678","Qantas",200)
def display4(passenger_name, *baggage_tuple):
    print("Passenger name:",passenger_name)
    total_wt=0
    for baggage_wt in baggage_tuple:
        total_wt+=baggage_wt
    print("Total baggage weight in kg:", total_wt)
print("-------------------------------------------------")
print("code-4: variable argument count")
display4("Jack",12,8,5)
#Uncomment and execute the below function call statements one by one and observe the output
display4("Chan",20,12)
display4("Henry",23)
'''

# Kwargs:
'''
def print_three_things(**kwargs):
    print(f"First: {kwargs['first']}")
    print(f"Second: {kwargs['second']}")
    print(f"Third: {kwargs['third']}")
arguments={'first': 'Ice Cream', 'second': 'Pizza', 'third': 'Burger'}
print_three_things(**arguments)
'''

# Global vs Local Variables:
wt_limit=30
def baggage_check(baggage_wt):
    extra_baggage_charge=0
    if not(baggage_wt>=0 and baggage_wt<=wt_limit):
        extra_baggage=baggage_wt-wt_limit
        extra_baggage_charge=extra_baggage*100
    return extra_baggage_charge
def update_baggage_limit(new_wt_limit):
    wt_limit=new_wt_limit
    print("This airline now allows baggage limit till",wt_limit,"kgs")
print("This airline allows baggage limit till",wt_limit,"kgs")
print("Pay the extra baggage charge of",baggage_check(35),"rupees")
update_baggage_limit(45)
print(wt_limit)
print("Pay the extra baggage charge of",baggage_check(35),"rupees")

# Global vs Local Variables:
wt_limit=30
def baggage_check(baggage_wt):
    extra_baggage_charge=0
    if not(baggage_wt>=0 and baggage_wt<=wt_limit):
        extra_baggage=baggage_wt-wt_limit
        extra_baggage_charge=extra_baggage*100
    return extra_baggage_charge
def update_baggage_limit(new_wt_limit):
    global wt_limit  # Global variable is accessed
    wt_limit = new_wt_limit
    print("This airline now allows baggage limit till",wt_limit,"kgs")
print("This airline allows baggage limit till",wt_limit,"kgs")
print("Pay the extra baggage charge of",baggage_check(35),"rupees")
update_baggage_limit(45)
print(wt_limit)
print("Pay the extra baggage charge of",baggage_check(35),"rupees")

