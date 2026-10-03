a=int(input("Enter The number from which the fibonacci needs to be started-: "))


if(a==0):
        b=a+1
        prev=a
elif(a==1):
        b=a
        prev=a
else:
        b=a-1
        prev=a-1

i=1
nextno=0

print(a, end=" ")

while(i<11):
        if(a<2):
            nextno=prev+1
            a=b
            b=nextno
        if(a>1):
            nextno=prev+a
            prev=a
            
        print(nextno, end=" ")
        prev=a
        a=nextno
        i+=1
    

