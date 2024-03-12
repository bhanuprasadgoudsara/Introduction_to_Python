wt_limit=30                                            #global variable
def baggage_check(baggage_wt):
    extra_baggage_charge=0                             #local variable
    if not(baggage_wt>=0 and baggage_wt<=wt_limit):
        extra_baggage=baggage_wt - wt_limit            #local variable 
        extra_baggage_charge=extra_baggage*100
    return extra_baggage_charge

def update_baggage_limit(new_wt_limit):
    '''wt_limit=new_wt_limit'''    # Python does not allow modification of a global variable inside a function directly.
                                   # So this wt_limit is taken as a new local variable
    # start
    global wt_limit
    wt_limit = new_wt_limit
    # end
    
    '''  As it is available throughout the program,
        use of global variable should be restricted
        to avoid accidental misuse by developers and to minimize memory usage. '''
    
    ''' In cases where a global variable needs to be modified inside a function,
        like in function update_baggage_limit(),
        Python allows you to do that using the global keyword.'''

    
    print("This airline now allows baggage limit till",wt_limit,"kgs")
    
print("This airline allows baggage limit till",wt_limit,"kgs")
print("Pay the extra baggage charge of",baggage_check(35),"rupees")
update_baggage_limit(45)
print("Pay the extra baggage charge of",baggage_check(35),"rupees")

# Output 1:
'''
This airline allows baggage limit till 30 kgs
Pay the extra baggage charge of 500 rupees
This airline now allows baggage limit till 45 kgs
Pay the extra baggage charge of 500 rupees
'''

# Output 2:
'''
This airline allows baggage limit till 30 kgs
Pay the extra baggage charge of 500 rupees
This airline now allows baggage limit till 45 kgs
Pay the extra baggage charge of 0 rupees
'''
