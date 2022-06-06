#Q8
a=input("enter the string")
d=0
for i in range(0,len(a)):
    if a[i].isnumeric():
        d+=int(a[i])
print("the result of addition is :{}".format(d))    
    
