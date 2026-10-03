no=int(input("Enter the number-: "))
sum=0
while(no>0):
    y=no%10
    sum=sum+y
    no=no//10
print(f"The sum of digits of given number is {sum}. ") 