x=int(input("Enter The number whose factorial needs to be calculated:- "))
fact=1
i=1
while(i<(x+1)):
    fact=fact*i
    i+=1
print(f"The Factorial of {x} is {fact}. ")   
    