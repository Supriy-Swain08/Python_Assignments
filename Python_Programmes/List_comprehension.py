#List Comprehension

#1.For loop version
print("\n","using for loop")
result=[]
for i in range(11):
    result.append(i)
print(result)
print("\n","using list Comprehension")
print([i for i in range(11)])
#2._________________________________________
print("\n","Odd Number")
result2=[]
for i in range(11):
    if i%2!=0:
        result2.append(i)
print(result2)
print([i for i in range(11) if i%2!=0])
print("\n","Even Number")
print([i for i in range(11) if i%2==0])
#3.__________________________________________
print("\n","Odd no and even square")
print([i if i%2!=0 else i**2 for i in range(11)])
#4.__________________________________________
print("\n","Matrix Data 4*4 printing odd and even square")
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
for i in mat:
    for j in i:
        if(j%2!=0):
            print(j,"",end="")
        else:
            print(j**2,"",end="")
print("\n\n","By use of Comprehension Matrix Data 4*4 printing odd and even square")

print([[j**2 if j%2!=0 else j**3 for j in i ]for i in mat],"",end="")

#5__________________________________________
print("\n")
for i in range(0,8):
    for j in range(0,8):
        if(i==0 or i==7 or j==0 or j==7):
            print("[_____]",end="")
        else:
            print("[",j,i,"]",end="")
    print("\n")

    
