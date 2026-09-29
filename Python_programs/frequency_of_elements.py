list_1 = [1,2,3,1,1,4,3]
count_list = {}
count = 0
for i in list_1:
    if i in count_list:
        count_list[i] = count_list[i] + 1
    else:
        count_list[i] = 1

print(count_list)

