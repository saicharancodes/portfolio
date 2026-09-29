import math
n = int(input("enter the number\n"))
number = n
sum = 0
length = len(str(n))
print(length)
while n>0:
    digit = n%10
    sum = sum + digit**length
    n = n//10
if (number==sum):
    print("it is armstrong number")
else:
    print("not an armstrong number")
