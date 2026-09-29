n = 123
count = 0
while n > 0:
    n = n // 10  # (// -> it will return the integer part of the quotient)
                 # ( / -> it will return the float value of the quotient)
    count = count + 1
print("Number of digits:", count)

# Time complexity  : o(logn)

