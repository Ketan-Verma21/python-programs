#Q2
def creditcard(a):
    c=""
    for i in range(0,16):
        if i>=12:
            c+=a[i]
        else:
            c+='*'
    return c        

a=input("enter your cerdit card number :")
d=creditcard(a)
print("the result is :",d)
