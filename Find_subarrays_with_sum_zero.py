import numpy as np
import math
arr=[1, 2, -3, 3, -1, 2]
# arr=[-3, 1, 2, -3, 4, 0]
# arr= [4, -1, -3, 1, 2, -1]
ans=[sum(arr[:i+1]) for i in range(len(arr))]
sol=[]
print(ans)
if ans.index(0):
    sol.append(tuple([0,ans.index(0)]))
for i in range(len(ans)):
    if ans.count(ans[i])==2:
        result = np.where(np.array(ans) == ans[i])[0]
        sol.append(tuple(result))
    if ans.count(ans[i])>2:
        result = np.where(np.array(ans) == ans[i])[0]
        sol.append(tuple(result[0:1]))
    ans[i]=math.inf
print(sol)