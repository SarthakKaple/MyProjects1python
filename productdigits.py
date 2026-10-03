no=int(input("Enter the number-: "))
product=1
temp=no

while(temp>0):
    y=temp%10
    temp=temp//10
    product=product*y

print(f"The product of digits in the number {no} is {product}. ")
