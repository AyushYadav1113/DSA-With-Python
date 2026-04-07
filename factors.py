# n = int(input("Enter the number: "))
# for i in range(1, n + 1):
#     if n % i == 0:
#         print(i)

n = int(input("Enter the number: "))
result = []
for i in range(1, n//2):
    if n% i==0 :
        result.append(i)
result.append(n)
print(result)
