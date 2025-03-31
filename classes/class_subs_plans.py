# Class Subs_Plans
import datetime as dt
from classes.class_subscriptions import Subscriptions
from classes.class_plans import Plans
# Import the generic class
from classes.gclass import Gclass

class Subs_Plans(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # class attributes, identifier id, attribute must be the first on the list
    att = ['_id', '_subscriptions_id', '_plans_id', '_status', '_start_date']
    # Class header title
    header = 'Subs_Plans'
    # field description for use in, for example, input form
    des = ['Id','Subscriptions_Id','Plans_Id', 'Status', 'Start_Date']
    # Constructor: Called when an object is instantiated
    def __init__(self, id, subscriptions_id, plans_id, start_date,status):
        super().__init__()
        # Object attributes
        # Check the customer and devices referential integrity
        subscriptions_id = int(subscriptions_id)
        plans_id = int(plans_id)
        if subscriptions_id in Subscriptions.lst:
            if plans_id in Plans.lst:
                id = Subscriptions.get_id(id)
                self._id = id
                self._subscriptions_id = subscriptions_id
                self._plans_id = plans_id
                self._status = status
                self._start_date = dt.datetime.strptime(start_date,'%Y/%m/%d')
                # Add the new object to the Subscription list
                Subs_Plans.obj[id] = self
                Subs_Plans.lst.append(id)
            else:
                print('Plans ', plans_id, ' not found')
        else:
            print('Subscription ', subscriptions_id, ' not found')
    # Object properties
    # id property getter method
    @property
    def id(self):
        return self._id
    # subscription_id property getter method
    @property
    def subscription_id(self):
        return self._subscriptions_id
    # plans_id property getter method
    @property
    def plans_id(self):
        return self._plans_id
    # status property getter method
    @property
    def status(self):
        return self._status
    # start_date property getter method
    @property
    def start_date(self):
        return self._start_date
    
    @id.setter 
    def id(self,new_id):
        self._id = new_id
        return self._id
    
    @subscription_id.setter 
    def subscription_id(self,new_subscription_id):
        self._subscription_id = new_subscription_id
        return self._subscription_id
    
    @plans_id.setter 
    def plans_id(self,new_plans_id):
        self._plans_id = new_plans_id
        return self._plans_id
    
    @status.setter 
    def status(self,new_status):
        self._status = new_status
        return self._status
    
    @start_date.setter 
    def start_date(self,new_start_date):
        self._start_date = new_start_date
        return self._start_date
  