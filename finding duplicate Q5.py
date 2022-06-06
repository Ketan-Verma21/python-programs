#Q5
print("start entering the numbers")
b=[]
for i in range(0,100):
    c=input()
    b.append(c)
for i in range(0,len(b)):
    for j in range(i+1,len(b)):
        if b[i]==b[j] :
            print("the number which is repeated is : {}".format(b[i]))
            break
        else :
            continue
