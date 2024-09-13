arr = [16, 17, 4, 3, 5, 2]
print('Leaders:',[arr[i] for i in range(len(arr)-1) if arr[i]>max(arr[i+1:])]+[arr[len(arr)-1]])