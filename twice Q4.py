#Q4
def string(a):
    c=""
    for i in range(0,len(a)):
        c+=2*a[i]
    return c    

a=input("enter the string:")
b=string(a)
print("the result is ",b)

