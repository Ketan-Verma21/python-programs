#Q3
def operator(a,b,c):
    if b=='+':
        return a+c
    elif b=='-':
        return a-c
    elif b=='/':
        return a/c
    else :
        return a or c
    
a=int(input("enter the first number :"))
b=input("enter one of  the operator in (+,-,/,or)")
c=int(input("enter the second number:"))
d=operator(a,b,c)
print("the result is :",d)

