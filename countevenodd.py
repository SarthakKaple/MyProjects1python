no=int(input("Enter the number-: "))
even=0
odd=0
temp=no

while(temp>0):
    n=temp%10
    temp=temp//10
    if((n%2)==0):
        even=even+1
    else:
        odd=odd+1

if(no==0):
    even=1    

print(f"The number {no} has {even} even digits and {odd} odd digits. ")

