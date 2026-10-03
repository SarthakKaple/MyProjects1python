x=int(input("Enter the Number-: ")) 

newno=0
turns=0
temp=x

while(x>9):
    x=x//10
    turns=turns+1

turns=turns+1
i=turns-1

while(temp>0):
    y=temp%10
    temp=temp//10
    newno=newno+ y*(10**i)
    i-=1
    
print(f"The reversed number is {newno}. ")