no1=int(input("Enter The first number-: "))
no2=int(input("Enter the second number-: "))
i=1
common=0

if(no1>no2):
    small=no2
else:
    small=no1

while(i<(small+1)):
    if(no1%i==0 and no2%i==0):
        common=i
    i+=1
    

print(f"The hcf of given numbers is {common}. ")