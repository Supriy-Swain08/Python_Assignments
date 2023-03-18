#Question 1
list_b=[6,4,6,1,2,2]
mylist=[9,3,6,1,5,0,8,2,4,7]
t=()
result=[]
for i in list_b:
    result.append((i,mylist.index(i)))
print(result)

print("\n\n\nBy Using Comprehension")
print([(i,mylist.index(i)) for i in list_b])
print({i:mylist.index(i) for i in list_b})
#Question 2
print("\n\n\nQuestion 2")
stopwords=['for','a','of','the','and','to','in','on','with']
sentence=["a new world record was set",
           "in the holy city of ayodhya",
           "on the eve of diwali on teusday",
           "with over three lakhs diya or earthen lamps",
           "lit up simultaneously on the bank of river sarayu river"]
rowdata=[]
senten=[]
for i in sentence:
    for j in i.split():
        if j not in stopwords:
            print(j,end=" ")
    print()
print("\n\n\nQuestion 2 by in a list")

for i in sentence:
    rowdata=[]
    for j in i.split():
        if j not in stopwords:
            rowdata.append(j)
    senten.append(rowdata)
print(senten)

        
print("\n\n\nQuestion 2 bt list comprehension")
[print(j,end=" ") for i in sentence for j in i.split() if j not in stopwords]
print("\n\n\nQuestion 3")

#Question 3
list1=['3','2','6','5','1','4','8','9']
list1=list(map(int,list1))
a=list1.index(5)
b=list1.index(8)
lis2=sum(list1[0:a])
lis3=sum(list1[b+1:])
print(lis2+lis3)
integer=int("".join(list(map(str,list1[a:b+1]))))
print(integer+lis2+lis3)



print("\n\n\nQuestion 4")

#Question 4
'''inp=input().split(",")
stt=[]
num=[]
for i in inp:
    s1,n=i.split(":")
    stt.append(s1)
    num.append(n)
def rotate(s,n):
    sum=0
    for i in n:
        sum+=int(i)**2
    if(sum%2==0):
        return s[-1]+s[:-1]
    else:
        return s[2:]+s[:2]
for i in range(len(num)):
    print(rotate(stt[i],num[i]))

'''
print("\n\n\nQuestion 5")
#Question 5
n=int(input())
l=[]
sum=0
for i in range(0,9):
    l.append(n+i)
def isprime(a):
    for j in range(2,a):
        if(a%j==0):
            return 0
        else:
            return 1
def largeprime(m):
    for i in range(m,0,-1):
        if m%i==0 :
            if(isprime(i)):
                return i
            else:
                continue
        else:
            continue
l=list(map(int,l))
print(l)
for c in l:
    sum+=largeprime(c)
print(sum)
            


