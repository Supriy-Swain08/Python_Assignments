#Decision making Questions
n=int(input())
if n%3==0 and n%5==0:
    print("multiple of both")
elif n%5==0:
    print("multiple of 5")
elif n%3==0:
    print("multiple of 3")
else:
    print("invalid")
