n=int(input("Enter How many Toffe u want"))
i=1
stock=10
while i<=n:
    if i<=stock:
        print(" Please Collect toffe=",i)
    else:
        print("Out of stock")
        break
    i=i+1
else:
    print("thank u please visit again")