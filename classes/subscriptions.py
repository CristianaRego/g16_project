# Class Subscriptions
import datetime as dt
from classes.devices import Devices
from classes.customer import Customer
from classes.plans import Plans
# Import the generic class
from classes.gclass import Gclass

class Subscriptions(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # class attributes, identifier id, attribute must be the first on the list
    att = ['_id', '_plans_id', '_customer_id', '_start_date', '_status']
    # Class header title
    header = 'Subscriptions'
    # field description for use in, for example, input form
    des = ['Id','Plans_Id','Customer_Id', 'Start_Date', 'Status']
    # Constructor: Called when an object is instantiated
    def __init__(self, id, plans_id, customer_id, start_date, status):
        super().__init__()
        # Object attributes
        # Check the customer and devices referential integrity
        customer_id = int(customer_id)
        plans_id = int(plans_id)
        if int(customer_id) in Customer.lst:
            if int(plans_id) in Plans.lst:
                id = Customer.get_id(id)
                self._id = id
                self._customer_id = int(customer_id)
                self._plans_id = int(plans_id)
                temp = list(map(int,start_date.split('/')))
                self._start_date = dt.date(temp[0],temp[1],temp[2])
                self._status = status
                # Add the new object to the Subscription list
                Subscriptions.obj[id] = self
                Subscriptions.lst.append(id)
            else:
                print('Plans ', plans_id, ' not found')
        else:
            print('Customer ', customer_id, ' not found')
    # Object properties
    # id property getter method
    @property
    def id(self):
        return self._id
    
    # customer_id property getter method
    @property
    def customer_id(self):
        return self._customer_id
    
    # plans_id property getter method
    @property
    def plans_id(self):
        return self._plans_id
    
    # start_date property getter method
    @property
    def start_date(self):
        return self._start_date
    
    # status property getter method
    @property
    def status(self):
        return self._status
    
    
    
    @id.setter 
    def id(self,new_id):
        self._id = new_id
        return self._id
    
    @customer_id.setter 
    def customer_id(self,new_customer_id):
        self._customer_id = new_customer_id
        return self._customer_id
    
    @plans_id.setter 
    def plans_id(self,new_plans_id):
        self._plans_id = new_plans_id
        return self._plans_id
    
    @start_date.setter 
    def start_date(self,new_start_date):
        self._start_date = new_start_date
        return self._start_date
    
    @status.setter 
    def status(self,new_status):
        self._status = new_status
        return self._status
  