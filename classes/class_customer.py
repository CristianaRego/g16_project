#Class Customer manteve-se Class Customer


#removi os setters, acho que após uma subscription em princípio não se 
#alterarão os dados de uma determinada fidelização


#também acrescentei o datetime para formatarmos dados temporais, mas podemos
#retirar se virem que não é útil ordenar dados por ordem de aparecimento.
import datetime 
from classes.gclass import Gclass

class Customer(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # class attributes, identifier attribute 'id' must be the first on the list
    att = ['_id','_email','_signup_date']
    # Class header title
    header = 'Customer'
    # field description for use in, for example, input form
    des = ['Id','Email','Signup_Date']
    # Constructor: Called when an object is instantiated
    #Cristiana: retirei o atributo phone e adicionei o name
    def __init__(self, id, name, email, signup_date):
        super().__init__()
        # Object attributes
        id = Customer.get_id(id)
        self._id = id
        self._name = name
        self._email = email
        temp = list(map(int,signup_date.split('/')))
        self._signup_date = datetime.date(temp[0],temp[1],temp[2])
        # Add the new object to the Customer's list
        Customer.obj[id] = self
        Customer.lst.append(id)
    
    # Object properties
    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @property
    def signup_date(self):
        return self._signup_date
    
#Cristiana: acrescentei o setter do email pq o cliente pode mudar de endereço de email após a fidelização

    @id.setter 
    def id(self,new_id):
        self._id = new_id
        return self._id

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