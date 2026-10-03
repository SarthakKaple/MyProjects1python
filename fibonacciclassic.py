a=int(input("Enter The number from which the fibonacci needs to be started-: "))

prev=0
current=1
found=False
nextno=0

while((current)<=(a)):
    if(current==a):
        found=True
        break

    nextno=prev+current
    prev=current
    current=nextno

if(a==0):
    found=True
    prev=0
    current=1

if found:
    print(a, end=" ")
    

    for i in range(9):
         nextno = prev + current 
         print(nextno, end=" ") 
         prev=current
         current=nextno

else: print(f"{a} is not a Fibonacci number.")



