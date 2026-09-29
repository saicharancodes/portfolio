number = 123
reverse = 0
while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10
print("Reversed Number:", reverse)

# Time complexity  : o(logn)

#leetcode code which i solvded
# class Solution:
#     def reverse(self, x: int) -> int:
#         reverse = 0
#         if x < 0:
#            sign = -1
#         else:
#             sign = 1
#         x = abs(x)
#         while (x>0):
#             digit = x%10
#             reverse = (reverse * 10) + digit
#             x = x//10
#         if -2**31 <= sign * reverse <= 2**31:
#             return sign * reverse
#         else:
#             return 0
