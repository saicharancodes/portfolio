arr = [14,9,15,12,6,8,13]
n = len(arr)
for i in range(1,n):
    for j in range(i,0,-1):
        if arr[j]< arr[j-1]:
            temp = arr[j]
            arr[j] = arr[j-1]
            arr[j-1] = temp
        else:
            continue
print (arr)
