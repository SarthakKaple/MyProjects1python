no=int(input("Enter the number-: "))
smallest=10
temp=no

while(temp>0):
    digit=temp%10
    temp=temp//10
    if(digit<smallest):
        smallest=digit
    

print(f"The largest digit in the given number is {smallest}. ") 