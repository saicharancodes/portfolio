#largest element in an array
# arr = [10,3,4,35]
# max = arr[0]
# for i in range(1,len(arr)):
#     if(arr[i] > max):
#         max = arr[i]

# print(max)

#-------------------------------------------------
#second largest element in an array
# arr = [1,2,4,7,7,5]
# max = arr[0]
# secondlargest = -1
# for i in range (1,len(arr)):
#     if(arr[i] > max):
#         # if arr[i] > secondlargest:
#             secondlargest = max
        
#             max = arr[i]

#     if(arr[i] < max and arr[i] > secondlargest):
#          secondlargest = arr[i]
# print(secondlargest)


#-------------------------------------------------

#check if the array is sorted
# arr = [1,2,4,6,7,8]
# for i in range(0,len(arr)-1):
#     if(arr[i]<arr[i+1]):
#         continue
#     else:
#         print("array is not sorted")
#         break

#-------------------------------------------------

# remove duplicates in a sorted array (two pointer approach)
# arr = [1,1,2,2,2,3,3]
# n = len(arr)
# i=0
# j=1
# while (j<n):
#     if(arr[j]==arr[i]):
#         j = j+1
#     else:
#         arr[i+1] = arr[j]
#         i = i + 1
    
# print(arr)

#-------------------------------------------------

#left rotate an array by one place
# arr = [1,2,3,4,5]

# approach 1:

# n=len(arr)
# for i in range(0,n-1):
#     temp = arr[i+1]
#     arr[i+1] = arr[i]
#     arr[i] = temp
# print(arr)

# approach 2:

# n = len(arr)
# temp = arr[0]
# for i in range (1,n):
#     arr[i-1] = arr[i]
# arr[n-1] = temp
# print(arr)

#-------------------------------------------------

#reverse the whole array
# arr = [1,2,3,4,5]
# start = 0
# end = len(arr)-1
# while(start < end):
#     temp = arr[start]
#     arr[start] = arr[end]
#     arr[end] = temp
#     start +=1
#     end-=1
# print(arr)

#-------------------------------------------------

#move zeroes to end of an array
# arr = [1,0,2,3,0,0,4,5]
# n = len(arr)
# j= -1
# for i in range(0,len(arr)):
#     if (arr[i] == 0):
#         break
# j = i
# i = j + 1
# for k in range (i,n):
#     if(arr[k]!=0):
#         temp = arr[k]
#         arr[k] = arr[j]
#         arr[j] = temp
#         j = j + 1
# print( arr)

#-------------------------------------------------   

#find missing number
# arr = [1,2,3,4,6,7,8]
# # approach - 1
# n = 8
# # arr_sum = 0
# # sum = (n*(n+1))//2
# # for i in range(0,len(arr)):
# #     arr_sum = arr_sum + arr[i]
# # missing_number = sum - arr_sum
# # print(missing_number)

# #approach-2(using xor)
# s1 = 0
# s2 = 0
# for i in range(0,len(arr)):
#     s1= s1 ^ arr[i]
# for i in range(1,n+1):
#     s2 = s2 ^ i
# print(s1 ^ s2)

#-------------------------------------------------

#max consecutive ones
# arr = [1,1,0,1,1,1,0,1,1]
# max = 0
# count = 0
# for i in range(0,len(arr)):
#     if(arr[i] == 1):
#         count += 1
#         if (count>max):
#             max = count
#     else:
#         count = 0
# print(max)

#-------------------------------------------------

#longest subarray with sum k
# -- Brute force 
# arr = [1,2,3,2,2,1,4,2,3]
# max = 0
# for i in range(0,len(arr)):
#     sum = 0
#     for j in range(i,len(arr)):
#         sum = sum + arr[j]
#         if(sum == 4 and ((j-i+1)>max)):
#             max = j-i+1
#         elif sum > 4:  
#             break
# print(max)

# --Better solution using prefix sum approach
# time complexity = 0(n)
# arr = [1,-1,2,3]
# hs = {}
# sum = 0
# res = 0
# k=5
# for i in range(0,len(arr)):
#     sum = sum +arr[i]
#     if sum == k:
#         temp = i+1
#         if(temp> res):
#             res = temp
#     if sum >= k:
#         prefix_sum = sum - k
#         if prefix_sum in hs:
#             temp = i - hs[prefix_sum]
#             if(temp > res):
#                 res = temp
#     if sum not in hs:
#         hs[sum] = i
# print(res)

#optimal solution
# time complexity = 0(2n)
# left=0
# right =0
# sum=0
# arr = [1,2,3,1,1,1,1,3,3]
# k = 6
# res = 0
# while(right<len(arr)):
#     sum = sum + arr[right]

#     while(left<=right and sum>k):
#             sum = sum - arr[left]
#             left = left + 1
#     if(sum == k):
#             temp = right-left + 1
#             res = max(res,temp)
#     right=right + 1
# print(res)

#-------------------------------------------------
#two sum = two pointer approach and i think we already know hashmap approach so i didnt wrote here
# arr = [2,6,5,8,12]
# target = 14
# hs =[]
# arr.sort()
# sum = 0
# left = 0
# right = len(arr)-1
# while(left<right):
#     sum = arr[left] + arr[right]
#     if sum > target:
#         right = right -1
#     elif sum <target:
#         left = left+1
#     elif sum == target:
#         hs.append([arr[left],arr[right]])
#         left = left + 1
# print(hs)

#-------------------------------------------------
# maximum subarray sum
# arr = [-2,-3,1,5,5,-3,-2,1,5,-3]
# max = arr[0]
# sum = 0
# for i in range(0,len(arr)):
#     sum = sum + arr[i]
#     if(sum>0):
#         if(sum > max):
#             max = sum
#     else:
#         sum = 0
# print(max)


# maximum contiguous subaary
arr = [2,-4,3,4,7,-18]

start = 0
end = 0
sum = 0
max = 0
for i in range(0,len(arr)):
    sum = sum + arr[i]
    if(sum > 0):
        if(sum>max):
            ansstart = start
            max = sum
            end = i
    else:
        start = i
        sum = 0
print(ansstart)
print(end)


# max = arr[0]
# sum = 0
# start = 0
# for i in range(0,len(arr)):
#     sum = sum + arr[i]
#     if(sum>0):
#         if(sum > max):
#             ansstart = start 
#             end = i
#             max = sum
#     else:
#         start = i
#         sum = 0
# print(max)
# for el in range(ansstart,end+1):
#     print(arr[el])

#-------------------------------------------------
# 3sum
# arr = [-1,0,1,2,-1,-4]
# hs = []
# sub_set = []
# res = []
# sum = 0
# for i in range(0,len(arr)):
#     hs = []
#     for j in range(i+1,len(arr)):
#         k = -(arr[i] + arr[j])
#         if k in hs:
#             sub_set.append([arr[i],arr[j],k])
#             sub_set.sort()
#             if sub_set not in res:
#                 res.append(sub_set)
#         else:
#             hs.append(j)

# print(res)


#-------------------------------------------------
#longest consecutive sequence
# arr = [102,4,100,1,101,3,2,1,1,103,104,105]
# hs = set()
# max = 0
# for i in range(0,len(arr)):
#     hs.add(arr[i])

# for i in range(0,len(arr)):
#     if(arr[i]-1 in hs):
#         continue
#     else:
#         count = 0
#         temp = arr[i]
#         while(temp in hs):
#             count = count +1 
#             temp = temp + 1
#         if(count > max):
#             max = count
# print(max)

#2nd approach 
# arr = [101,102,103,104,105,1,2,3,4,5,6]
# arr.sort()
# max = 0
# count = 1
# for i in range(1,len(arr)):
#     if(arr[i]-1 == arr[i-1]):
#         count = count +1
#         if(count > max):
#             max = count
#     else:
#         count = 1

# print(max)


#-------------------------------------------------
arr = [2,3,-2,4,-2,-1]
#this approach will work only if we have one negative variable
# max = 0
# temp = 1
# for i in range(0,len(arr)):
#     temp = temp * arr[i]
#     if(temp<0):
#         temp = 1
#     else:
#         if(temp>max):
#             max = temp
# print(max)

#this approach will work for everything
# max = 0
# temp = 1
# prefix_mul = 1
# sufix_mul = 1
# for i in range(0,len(arr)):
#     prefix_mul = prefix_mul * arr[i]
#     if(prefix_mul > max):
#         max = prefix_mul
#     if(prefix_mul == 0):
#         prefix_mul = 1
# for i in range(len(arr)-1,-1):
#     sufix_mul = sufix_mul * arr[i]
#     if(sufix_mul > max):
#         max = sufix_mul
#     if(sufix_mul == 0):
#         sufix_mul = 1
# print(max)


# longest substring without repeating charcaters
# brute force approach
# inp = 'abcabced'
# max = 0
# for i in range(0,len(inp)):
#     ls = []
#     count = 0
#     for j in range(i,len(inp)):
#         if inp[j] not in ls:
#             count = count + 1
#             if(count > max):
#                 max = count
#         else:
#             break
#         ls.append(inp[j])
# print(max)

#optimal
# inp = 'bbabbb'
# max = 0
# left = 0
# right = 0
# count = 0
# hs = {}
# while(right < len(inp)):
#     if(inp[right] not in hs):
#         count = right - left + 1
#         if(count > max):
#             max = count
#     else:
#         left = hs[inp[right]] + 1
#     hs[inp[right]] = right
#     right = right + 1
# print(max)
