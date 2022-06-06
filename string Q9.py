#Q9
a=input("enter the string")
d=[]
b=""
for i in range(0,len(a)):
    d.append(a[i])
d.sort()
for i in d:
    b+=i
print(b)    
    
