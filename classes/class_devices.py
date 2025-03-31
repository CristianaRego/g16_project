# Class Devices
# Import the generic class
from classes.gclass import Gclass

class Devices(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # class attributes, identifier attribute 'id' must be the first on the list
    att = ['_id','_name', '_os']
    # Class header title
    header = 'Devices'
    # field description for use in, for example, input form
    des = ['Id','Name', 'OS']
    # Constructor: Called when an object is instantiated
    def __init__(self, id, device_name, os):
        super().__init__()
        # Object attributes
        id = Devices.get_id(id)
        self._id = id
        self._name = device_name
        self._os= os
        # Add the new object to the Devices list
        Devices.obj[id] = self
        Devices.lst.append(id)
    
    # Object properties
    # id property getter method
    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name
    
    @property
    def os(self):
        return self._os
    
    @id.setter 
    def id(self,new_id):
        self._id = new_id
        return self._id
    
    @name.setter 
    def name(self,new_name):
        self._name = new_name
        return self._name
    
    @os.setter 
    def os(self,new_os):
        self._os = new_os
        return self._os