#Class Customer
import datetime 
from classes.devices import Devices
from classes.gclass import Gclass

class Customer(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # class attributes, identifier attribute 'id' must be the first on the list
    att = ['_id', 'devices_id', 'name', '_email', '_signup_date', '_foto']
    # Class header title
    header = 'Customer'
    # field description for use in, for example, input form
    des = ['Id', 'Devices_Id', 'Name', 'Email', 'Signup_Date', 'Foto']
    # Constructor: Called when an object is instantiated


    def __init__(self, id, devices_id, name, email, signup_date, foto):
        super().__init__()
        # Object attributes
        id = Customer.get_id(id)
        if int(devices_id) in Devices.lst:
            self._id = id
            self._devices_id= int(devices_id)
            self._name = name
            self._email = email
            temp = list(map(int,signup_date.split('/')))
            self._signup_date = datetime.date(temp[0],temp[1],temp[2])
            self._foto= foto
            # Add the new object to the Customer's list
            Customer.obj[id] = self
            Customer.lst.append(id)
        else:
            print('Device ', devices_id, ' not found')
    
    # Object properties
    @property
    def id(self):
        return self._id
    
    @property
    def devices_id(self):
        return self._devices_id
    
    @property
    def name(self):
        return self._name
    
    @property
    def email(self):
        return self._email

    @property
    def signup_date(self):
        return self._signup_date
    
    @property
    def foto(self):
        return self._foto
    
    @id.setter 
    def id(self,new_id):
        self._id = new_id
        return self._id

    @devices_id.setter 
    def devices_id(self,new_id):
        self._devices_id = new_id
        return self._devices_id
    
    @name.setter 
    def name(self,new_name):
        self._name = new_name
        return self._name
    
    @email.setter 
    def email(self,new_email):
        self._email = new_email
        return self._email
    
    @signup_date.setter 
    def signup_date(self,new_signup_date):
        self._signup_date = new_signup_date
        return self._signup_date
    
    @foto.setter 
    def foto(self,foto):
        self._foto=foto