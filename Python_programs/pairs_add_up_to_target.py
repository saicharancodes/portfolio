# arr= [1,2,3,4,3,-1,1]
# target = 6
# output = []
# used = []
# for el in input_1:
#     sub_list = []
#     another_el = target - el
#     if another_el in input_1 and another_el not in used:
#         sub_list.append(el)
#         sub_list.append(another_el)
#         used.append(el)
#         output.append(sub_list)
# print(output)

# hs = {}
# target = 6
# final = []
# for i in range(0,len(arr)):
#     temp = target - arr[i]
#     subset = []
#     if(temp in hs):
#         subset.append(arr[i])
#         subset.append(temp)
#         final.append(subset)
#     else:
#         hs[arr[i]] = i
# print(final)


arr= [-1,0,3,2,6]
hs = {}

res = []
target = 5
arr.sort()
left = 0
right = len(arr)-1
while(left < right ):
    if((arr[left] + arr[right]) == target):
        add = []
        add.append(arr[left])
        add.append(arr[right])
        res.append(add)
        left = left + 1
        right = right - 1
    elif((arr[left] + arr[right]) > target):
        right = right - 1
    else:
        left = left + 1
print(res)


























