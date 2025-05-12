# Class Plans
# Import the generic class
from classes.gclass import Gclass

class Plans(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # class attributes, identifier attribute 'id' must be the first on the list
    att = ['_id','_name','_data_limit', '_monthly_fee']
    # Class header title
    header = 'Plans'
    # field description for use in, for example, input form
    des = ['Id','Name','Data_Limit', 'Monthly_Fee:']
    # Constructor: Called when an object is instantiated
    def __init__(self, id, plans_name, data_limit, monthly_fee):
        super().__init__()
        # Object attributes
        id = Plans.get_id(id)
        self._id = id
        self._name = plans_name
        self._data_limit = data_limit
        self._monthly_fee= monthly_fee
        # Add the new object to the Order list
        Plans.obj[id] = self
        Plans.lst.append(id)
            
    # Object properties
    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    @property
    def data_limit(self):
        return self._data_limit
    
    @property
    def monthly_fee(self):
        return self._monthly_fee
    
    @id.setter 
    def id(self,new_id):
        self._id = new_id
        return self._id
    
    @name.setter 
    def name(self,new_name):
        self._name = new_name
        return self._name
    
    @data_limit.setter 
    def data_limit(self,new_data_limit):
        self._data_limit = new_data_limit
        return self._data_limit
    
    @monthly_fee.setter 
    def monthly_fee(self,new_monthly_fee):
        self._monthly_fee = new_monthly_fee
        return self._monthly_fee
    
    