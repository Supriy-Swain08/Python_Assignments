#Example:1
'''inp=input()
l=0
d=0
for i in inp:    
    if (i.isalpha()):
        l+=1
    elif (i.isdigit()):
        d=d+1
print([l,d])
'''
#Example:2
'''lis=list(map(int,input().split()))
s=int(input())
c=0
d=len(lis)
for i in range(d-1):
    for j in range(i+1,d):
        if(lis[i]+lis[j])==s:
            c+=1
print(c)
'''
#Example:3
'''inp=input()
if(len(inp)<2):
    print("-1")
else:
    print(inp[0:2],inp[-2:])
'''
#Example:4
'''inp=input()
if(len(inp)<3):
    print(inp)
elif(inp[-3:]=="ing"):
    print(inp+"ly")
else:
    print(inp+"ing")'''
#Example:5
'''def check_double(number):
    num=2*number
    a=list(str(number))
    b=list(str(num))
    c=0
    if(len(a)==len(b)):
        for i in a:
            if(i in b):
                c+=1
        if(c==len(a)):
            return True

print(check_double(int(input())))'''
#Or
'''def check_double(number):
    a=list(str(number))
    b=list(str(2*number))
    a.sort()
    b.sort()
    if(a==b):
        return True
print(check_double(int(input())))'''
#Example:6
'''def findmorethanavg(tup):
    c=0
    avg=sum(list(tup))/len(tup)
    for i in tup:
        if(i>avg):
            c+=1
    return c/len(tup)*100
def generatefrequency(inp):
    list1=[]
    for i in range(0,25):
        list1.append(list(inp).count(i))
    print(list1)
def sortmarks(inp):
    print(sorted(inp))
inp=tuple(map(int,input().split()))
print(findmorethanavg(inp))
generatefrequency(inp)
sortmarks(inp)'''
#Example 7
'''dic={"merry":"god","christmas":"jul","and":"och","harry":"gott","new":"nytt","year":"ar"}
lis=list(dic.keys())
inp=input().split()
for i in inp:
    if(i in lis):
        print(dic[i],"",end="")
    else:
        print(i,"",end="")'''

#Example 8
'''def fun(a,b):
    lis=list(range(a,b))
    lis1=[]
    c=0
    for i in range(len(lis)):
        for j in range(i,len(lis)):
            lis1.append(lis[i:j+1])
            if(sum(lis[i:j+1])%2==1):
                c=c+1
    print(lis1)
    print(c)

fun(1,4)
'''







