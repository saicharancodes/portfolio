#Definition of a prime number: A prime number is a whole number greater than 1
#that has only two distinct positive divisors: \(1\) and the number itself.
import math
n = int(input("enter the number\n"))
dummy = 0
if n ==1:
    print("neither prime nor composite")
else:
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):
            dummy = 1
    if(dummy == 0):
        print("it is a prime number")
    else:
        print("it is not a prime number")
        
        
