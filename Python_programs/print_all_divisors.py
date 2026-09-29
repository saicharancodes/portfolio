import math
n= 36
for i in range(1,int(math.sqrt(n))+1):
    if n%i == 0:
        print(i)
        if n//i != i:
            print(n//i)