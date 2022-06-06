#Q6
c=int(input("enter the first number of the range :"))
h=int(input("enter the number upto which you have to find the prime :"))
b=[]
for i in range(c,h+1):
    a=0
    for j in range(2,i//2+1):
        if i%j==0:
            a+=1
            break
    if (a==0 and i!=1):
        print("%d" %i,end='  ')
    
    

    
            
