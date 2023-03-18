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
                return (i)
            else:
                continue
        else:
            continue
l=list(map(int,l))
print(l)
for c in l:
    sum+=largeprime(c)
print(sum)
