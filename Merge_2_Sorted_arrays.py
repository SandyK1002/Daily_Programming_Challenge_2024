arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]

while(min(arr2)<max(arr1)):
    max_idx = arr1.index(max(arr1))
    min_idx = arr2.index(min(arr2))
    arr1[max_idx], arr2[min_idx] = arr2[min_idx], arr1[max_idx]

arr1.sort()
arr2.sort()
print('arr1 =',arr1)
print('arr2 =',arr2)