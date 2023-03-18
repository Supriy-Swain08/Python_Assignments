#Functions
def function1():
    print("Its function 1")
def function2(num1,num2):
    print("num1",num1,"num2",num2)
def function3(a,b):
    return a+b
def function4(a,b):
    return int(a)+b
def function5(a,b):
    return a+b
function1()
function2(10,20)
print("Value returned:",function3(100,200))
print("Value returned:",function3(100,200.2))
print("Value returned:",function4('100',200.2))
print("Value returned:",function5('100 ','200.2'))

#1.Positional arguements
def fun1(n1,n2,n3,n4):
    print("number1",n1,"number2",n2,"number3",n3,"number4",n4)
fun1(10,20,30,40)#Can't give more or less no of arguements
#2.Keyword Arguements
def fun2(n1,n2,n3,n4):
    print("number1",n1,"number2",n2,"number3",n3,"number4",n4)
fun2(n4=10,n1=20,n2=30,n3=40)
#3.Default Arguements
def fun3(name,rollno,branch,collegename="GIETU"):
    print("Name",name,"\n","Roll",rollno,"rollno","Branch",branch,"College",collegename)
fun3("Supriya",76,"CSE")
fun3("Aniket",67,"CST")
fun3("Sibasantosh",70,"ECE")
#3.Variable no of Arguements
def fun4(*var):
    for i in var:
        print(i,end="")
fun4("Supriya",76,"CSE")
print()
fun4(10,20,30)

print()

def add(*var):
    sum=0
    for i in var:
        sum+=i
    return sum
print(add(10,20,30,40,50,60))
