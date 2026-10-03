no=int(input("Enter the Number:- "))
divisum=0
i=1
temp=no

while(no>i):
    if((temp%i)==0):
        divisum=divisum+i
    i+=1

if(divisum==no):
    print(f"The number {no} is a perfect number. ")
else:
    print(f"The number {no} is not a perfect number. ")

