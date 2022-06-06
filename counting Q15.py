#Q15
a=input("enter the string:")
b=0
c=0
d=0
for i in range(0,len(a)):
    if a[i].isdigit():
        b+=1
    elif a[i].isalpha():
        c+=1
    else :
        d+=1
print("the count of numeric terms is {} \n alphabet terms is {} \n special character is {}".format(b,c,d))        
