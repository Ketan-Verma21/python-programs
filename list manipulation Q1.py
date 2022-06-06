#Q1
def manipulation(d,e):
    if e=="asc":
        d.sort()
        return d
    elif e=="desc":
        d.sort(reverse=True)
        return d
    else :
        return d
    
a=int(input("enter the total number of elements which you want to wish to enter in the array :"))
d=[]
print("you can start inputing elements")
for i in range(0,a):#appending the elements in array
    c=input()
    d.append(c)
e=input("enter what do you want to do with array 1.asc  , 2. desc , 3. none :")

f=manipulation(d,e)
print("the result is :",f)
    
    
