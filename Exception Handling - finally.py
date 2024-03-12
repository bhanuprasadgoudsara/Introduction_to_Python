# finally

''' Sometimes in programming we need to execute some code
    irrespective of whether the primary program logic itself succeeds or fails to do its job.
    In Python we can achieve this using a finally block.
    A finally block of statement is an optional part of the try-except statements.
    A code written inside the finally block will ALWAYS be executed.
    finally block is majorly used to close the database connections in the programs which involves database connectivity.'''
balance = 1000
amount = "300Rs"

def take_card():
    print("Take the card out of ATM")

try:
    if balance >= int(amount):
        print("Withdraw")
    else:
        print("Invalid amount")
except TypeError:
    print("Type Error Occurred")
except ValueError:
    print("Value Error Occurred")
except:
    print("Some Error Occurred")
finally:
    take_card()
