n = int(input("Enter the number: "))
temp=n
rev=0
while(temp !=0):
    d=temp%10
    rev=rev*10+d
    temp=temp//10

if rev==n:
        print("The number is palindrome number")
else :
        print("The number is not palindrome number")