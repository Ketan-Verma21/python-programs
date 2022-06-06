#Q7
import statistics
a=int(input("enter how much long array you have to input :"))
b=[]
print("start inputting the elements in array :")
for i in range(0,a):
    c=input()
    b.append(c)
    
d=statistics.mode(b)
print("the frequent element in the string is {}".format(d))

    
    
