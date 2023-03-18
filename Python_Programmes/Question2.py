'''need=int(input())
curr=input()
if(curr=="Euro"):
    print(need*0.01417)
elif curr=="British Pound":
    print(need*0.100)
elif curr=="Australian Dollar":
    print(need*0.02140)
elif curr=="Canadian Dollar":
    print(need*0.02027)
else:
    print("Invalid Input")
'''
'''a=int(input())
b=int(input())
aprice=a*37550
bprice=b*37550.0/3
total=aprice+bprice+((aprice+bprice)*0.07)
print(total-total*0.10)'''
def require(one,five,need):
    required5=0
    left=0
    if(five>=int(need/5)):
        required5=int(need/5)
    else:
        required5=five
    left=need-required5*5
    rq=left+required5
    if(rq>=one+five):
        print(required5,left)
    else:
        print("invalid")
require(int(input()),int(input()),int(input()))
    
        
