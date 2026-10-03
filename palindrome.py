x=int(input("Enter the Number-: ")) 
temp=x
rev=0

while(temp>0):
    digit=temp%10
    rev=rev*10+digit
    temp=temp//10
    
if(rev==x):
    print(f"The number {x} is palindrome. ")
else:
    print(f"The number {x} is not a palindrome. ")
print(f"Because the reverse of the number is {rev}")  
