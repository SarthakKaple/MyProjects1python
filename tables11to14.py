i=1
x=11
while(i<=10):
    while(x!=15):
        print(x*i, end=" ")
        if(i==10):
            i=1
            print(".")
            break
        i+=1
    x+=1

    