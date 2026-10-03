no=int(input("Enter the number-: "))
i=1
esum=0
osum=0
while(i<=no):
    if(i%2==0):
        esum=esum+i
    else:
        osum=osum+i
    i+=1
print(f"The sum of even numbers till {no} is {esum}. ")
print(f"The sum of odd numbers till {no} is {osum}. ")
