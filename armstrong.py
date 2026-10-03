x=int(input("Enter the number to be checked:- "))
temp=x
sum=0
k=x
digits=0

while(x>0):
    x=x//10
    digits+=1

while(temp>0):
    y=temp%10
    temp=temp//10
    sum=sum+(y**(digits))

if(sum==k):
    print(f"The number {k} is armstrong. ")
else:
    print(f"The number {k} is not armstrong. ")



