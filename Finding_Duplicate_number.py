arr=[3, 1, 3, 4, 2]
for i in range(len(arr)):
    if arr.count(arr[i]) == 2:
        print('Duplicate number:',arr[i])
        break