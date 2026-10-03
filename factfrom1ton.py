no=int(input("Enter the number till whose factorial needs to be calculated-: "))
i=1
fact=1
while(i<=no):
    fact=fact*i
    print(f"The factorial of {i} is {fact}. ")
    i+=1

