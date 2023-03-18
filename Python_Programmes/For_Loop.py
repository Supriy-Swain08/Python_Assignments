#For loop/range
for i in range(1,101):
    #range(start,end,step)
    print(i,end=' ')
print('\n')
for i in range(1,101,2):
    print(i,end=' ')
print('\n')
for i in range(2,101,2):
    print(i,end=' ')
print('\n')
for i in range(100,0,-1):
    print(i,end=' ')
print('\n')
for i in range(99,0,-2):
    print(i,end=' ')
print('\n')
for i in range(100,0,-2):
    print(i,end=' ')
print('\n')

#break statement
for i in range(1,101):
    if(i==50):
        break
    else:
        print(i,end=' ')
print('\n')
for i in range(1,101):
    if(i==50): 
        continue
    print(i,end=' ')
print('\n')
for i in range(1,101):
    if(i==50): 
        pass
    print(i,end=' ')
    
