x = int(input("enter a number"))
a=0
b=1
while(b<x):
    temp = a+b
    a = b
    b = temp
print(a,b)
if(x-a>b-x):
    print(b)
else:
    print(a)    
