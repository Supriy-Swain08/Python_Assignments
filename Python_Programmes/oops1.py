class shoes:
    def __init__(self,price,material):
        self.price=price
        self.material=material
    def __str__(self):
        return "Shoe with price:"+str(self.price)+"And material:"+self.material
s1=shoes(1000,'Canvas')
print("The unique id of object is ",id(s1))
print(s1)

print("\n,Question 2")
class Mobile:
    def display(self):
        print("Displaying details ")
    def purchase(self):
        self.display()
        print("Calculating Price")
Mobile().purchase()


print("\n,Question 3")
a=[]
b=[]
def find_sum(n):
    p=str(n)
    for i in range(0,len(p)):
        sum=0
        for j in range(i,len(p)):
            a.append(p[i:j+1])
    
    for m in a:
        sum=0
        for n in m:
            sum+=int(n)
        if(sum==10):
            b.append(m)
        else:
            sum=0
    return b
res=find_sum(3523014)
print(res)

print("\n,Question 4")
class Table:
    def __init__(self):
        self.no_of_legs=4
        self.glass_top=None
        self.wooden_top=None
        print(id(self))
dining_table=Table()
#print('dining_table:',id(dining_table))
back_table=Table()
print('Back_table:',id(back_table))
front_table=back_table
back_table=dining_table        
print(dining_table,back_table,front_table)

























            
