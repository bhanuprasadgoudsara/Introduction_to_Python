# Packages :
''' Let's asume that the manageFlights.py inside Flights package has below code:'''
'''
airline="Smart Airlines"
def add(no_of_flights):
    print(no_of_flights," flights added to the fleet")
'''
''' If we need to access the function add(), inside the ManageFights module is in some other module,
    then we can import the ManageFights  module and use it'''

# import can be done two ways:

# method 1:
from Flights import ManageFlights   # from packagename import modulename
ManageFlights.add(10)

# method 2:
import Flights.ManageFlights        # import packagename.modulename
Flights.ManageFlights.add(20)



#Package Naming Conflict:
''' Consider a scenario where two modules have the same name
    which are present in different packages and both of them have the same function ‘add’.
    Flights -> Manage.py -> add()
    Employees -> Manage.py -> add()

To avoid naming conflicts during import, we can use one of the below techniques:'''
# 1:
import Flights.Manage
import Employees.Manage
Flights.Manage.add(30)
Employees.Manage.add(40)

# 2:
from Flights import Manage as FManage
from Employees import Manage as EManage
FManage.add(50)
EManage.add(60)

# 3:
from Flights.Manage import add as add1
from Employees.Manage import add as add2
add1(70)
add2(80)

