# arr = [113,46,24,30,9]
# n = len(arr)
# for i in range(n-1,0,-1):
#     for j in range(0,i):
#         if(arr[j]>arr[j+1]):
#             temp = arr[j+1]
#             arr[j+1] = arr[j]
#             arr[j] = temp

# print(arr)
# import sys
# import os
# print(sys.path)
# # sys.path.insert(1, os.path.dirname(__file__))
# # from helper.test_helper import add
# # add(5)

# arr=[15,14,13,12]

# for i in range(len(arr),1,-1):
#     for j in range(0,i-1):
#         if(arr[j]>arr[j+1]):
#             arr[j],arr[j+1] = arr[j+1],arr[j]
# print(arr)

arr = [1,2,3]
print(arr[::-1])