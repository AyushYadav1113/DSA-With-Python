n = int(input("Enter the number: "))
temp =n
sum=0
while(temp!=0):
    d=temp%10
    sum += d*d*d
    temp=temp//10
if sum==n:
    print("The number is armstrong number")
else:
    print("The number is not armstrong number")