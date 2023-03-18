list=list(map(int,input().split()))
product=1
for i in list:
    product*=i
    if(i==7):
        product=1
        continue
if(product==1):
    print(-1)
else:
    print(product)
