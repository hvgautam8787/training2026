n=int(input("enter any number"))
orig=n
sum=0
while n>0:
    digit=n%10
    sum=sum+digit*digit*digit
    n=n//10

print("Sum of digit=",sum)
if orig==sum:
    print("armstrong no")
else:
    print("not armstrong")
