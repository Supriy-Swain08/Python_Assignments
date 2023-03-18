'''n=int(input())
def find_p(n):
    p=str(n)
    if(p==p[::-1]):
        print(n)
        return 0
    else:
        find_p(n+1)
    return 1
find_p(n+1)

print("\nMethod2")

def find_p(n):
    p=str(n)
    if(p==p[::-1]):
        return (n)
    else:
        find_p(n+1)
n=int(input())
print(find_p(n+1))'''

'''print("\nQuestion 2")
n=input().split(",")
dic={"p":"Pediatrics","o":"Orthopedics","e":"ENT"}
c=0
res='a'
for i in range(1,len(n),2):
    if(n.count(n[i])>c):
        c=c+1
        res=n[i]
print(dic[res])
'''

'''print("\nQuestion 3")
n1=input()
n2=input()
for i in n1:
    if(i in n2 and i!=" "):
        print(i,end="")
'''
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
    res=[[]]
    l=[]
    for i in range(0,len(name)-1):
        l.append(list(name[i],score[i]))
        res.append(l)
    print(res)



























