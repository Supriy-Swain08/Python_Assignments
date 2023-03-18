'''class Finance:
    def __init__(self,Id=0,Type=0,cost=0,Amount=0):
        self.__Id=Id
        self.__Type=Type
        self.__cost=cost
        self.__Amount=Amount
    def get__Id(self):
        return self.__Id
    def set__Id(self,n):
        self.__Id=n
    def get__Type(self):
        return self.__Type
    def set__Type(self,t):
        self.__Type=t
    def get__cost(self):
        return self.__cost
    def set__cost(self,c):
        self.__cost=c
    def check(self):
        if(self.__Type==2):
            self.__Amount=self.__cost+self.__cost*0.02
            print(self.__Amount)
        elif(self.__Type==4):
            self.__Amount=self.__cost+self.__cost*0.04
            print(self.__Amount)
        else:
            print("Not Valid")
o1=Finance()
o1.set__Id(int(input("Enter The Id:")))
o1.set__Type(int(input("Enter The Type:")))
o1.set__cost(int(input("Enter The cost:")))
print("\nEnterd Details Are:---------")
print("Entered Id is:",o1.get__Id(),"\n","Entered Type:",o1.get__Type(),"\n","Entered Cost:",o1.get__cost())
print("\n You have to pay:------")
o1.check()
'''
'''print("Question 2 For University")
class Student:
    def __init__(self):
        self.__student_id=None
        self.__marks=None
        self.__age=None
    def get__student_id(self):
        return self.__student_id
    def set__student_id(self,i):
        self.__student_id=i
    def get__marks(self):
        return self.__marks
    def set__marks(self,m):
        self.__marks=m
    def set__age(self,a):
        self.__age=a
    def get__age(self):
        return self.__age
    def validate_marks(self):
        if(self.__marks>64):
            return True
        else:
            return False
    def validate_age(self):
        if(self.__age>19):
            return True
        else:
            return False
o=Student()
o.set__student_id(int(input("Enter Student's Id:")))
o.set__marks(int(input("Enter Student's Marks:")))
o.set__age(int(input("Enter Student's Age:")))
print("\nEnterd Details Are:---------")
print("Entered Id is:",o.get__student_id(),"\n","Entered Mark:",o.get__marks(),"\n","Entered Age:",o.get__age())
if(o.validate_marks() and o.validate_age()):
    print("Enter Your Course Id:")
    course=int(input())
    if(course==1001):
        if(o.get__marks()>84):
            print("Calculated Fees is:",25575-25575*0.25)
        else:
            print("Calculated Fees is:",25575)
    elif(course==1002):
        if(o.get__marks()>84):
            print("Calculated Fees is:",15500-15500*0.25)
        else:
            print("Calculated Fees is:",15500)
else:
    print("Not Eligible")
'''
class Customer:
    def __init__(self,quantity):
        self.quantity=quantity
    def validate_quantity(self):#can order 1-5 pizzas
        if(self.quantity<6):
            return True
        else:
            print('You can not order more than 5 pizzas')
            return False
class Pizzaserviceclass(Customer):
    count=100
    def __init__(self,size,add_top):
        self.size=size
        self.add_top=add_top
    def validate_size(self,s):
        if(s=="small" or s=="medium"):
            return True
        else:
            return False
    def Topping_required(self,top):
        if(top=="yes"):
            return True
        else:
            return False
    def Pizza_cost(self):
        print(self.size,self.add_top)
quantity=int(input("Howmany Pizzas do you Want:"))
if(Customer(quantity).validate_quantity()):
    s=input("Which size do you want:")
    if(Pizzaserviceclass().validate_size(s)):
        top=input("Do you want Toppings:")
        if(cus.Topping_required):
            cus=Pizzaserviceclass(s,"Yes")
        else:
            cus=Pizzaserviceclass(s,"No")
            
    
        
    






















































