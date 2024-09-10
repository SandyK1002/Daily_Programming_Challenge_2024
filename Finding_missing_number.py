arr=[1,2,4,5]
for i in range(len(arr)):
    if arr[i]==i+1:
        continue
    else:
        print('Missing Number:',i+1)
        break
