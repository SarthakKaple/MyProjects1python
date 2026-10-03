x=int(input("Enter the Number-: ")) 
temp=x
rev=0

while(temp>0):
    digit=temp%10
    rev=rev*10+digit
    temp=temp//10
    
print(f"The reverse of the number {x} is {rev}. ")    
