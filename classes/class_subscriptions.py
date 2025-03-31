# Class Subscriptions
from classes.class_customer import Customer
from classes.class_devices import Devices
# Import the generic class
from classes.gclass import Gclass

class Subscriptions(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # class attributes, identifier id, attribute must be the first on the list
    att = ['_id', '_customer_id','_devices_id']
    # Class header title
    header = 'Subscriptions'
    # field description for use in, for example, input form
    des = ['Id','Customer_id','Devices_id']
    # Constructor: Called when an object is instantiated
    def __init__(self, id, customer_id, devices_id):
        super().__init__()
        # Object attributes
        # Check the customer and devices referential integrity
        customer_id = int(customer_id)
        devices_id = int(devices_id)
        if customer_id in Customer.lst:
            if devices_id in Devices.lst:
                id = Subscriptions.get_id(id)
                self._id = id
                self._customer_id = customer_id
                self._devices_id = devices_id
                # Add the new object to the Subscription list
                Subscriptions.obj[id] = self
                Subscriptions.lst.append(id)
            else:
                print('Device ', devices_id, ' not found')
        else:
            print('Customer ', customer_id, ' not found')
    # Object properties
    # id property getter method
    @property
    def id(self):
        return self._id
    # order property getter method
    @property
    def customer_id(self):
        return self._customer_id
    # product property getter method
    @property
    def devices_id(self):
        return self._devices_id
    
    @id.setter 
    def id(self,new_id):
        self._id = new_id
        return self._id
    
    @customer_id.setter 
    def customer_id(self,new_customer_id):
        self._customer_id = new_customer_id
        return self._customer_id
    
    @devices_id.setter 
    def id(self,new_devices_id):
        self._devices_id = new_devices_id
        return self._devices_id
  