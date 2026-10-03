no1=int(input("Enter The first number-: "))
no2=int(input("Enter the second number-: "))

i=1
j=1
lcm=0

while((no1*i)!=(no2*j)):
    if((no1*i)<(no2*j)):
        i+=1
    else:
        j+=1

lcm=(no1*i)

print(f"The LCM of the given numbers is {lcm}. ")