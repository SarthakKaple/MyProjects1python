no=int(input("Enter the number-: "))
largest=0
temp=no

while(temp>0):
    digit=temp%10
    temp=temp//10
    if(digit>largest):
        largest=digit
    

print(f"The largest digit in the given number is {largest}. ")