arr=[0,1,2,1,0,2,1,0]
n=len(arr)

#  Sorting starts here

zero,one,two=0,0,0
for i in arr:
    if i==0:
        zero+=1
    elif i==1:
        one+=1
    elif i==2:
        two+=1

ans = [0]*zero + [1]*one + [2]*two

print('The sorted array, arranged in the increasing order of 0s, 1s and 2s is: ',ans)
