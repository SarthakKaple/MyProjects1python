x=int(input("Enter the number-: "))
turns=0
while(x>9):
    x=x//10
    turns=turns+1
turns=turns+1
print(f"The no: of digits in the entered number is {turns}. ")

