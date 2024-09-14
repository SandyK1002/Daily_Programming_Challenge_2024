arr=[1, 2, -3, 3, -1, 2]
# arr=[4, -1, -3, 1, 2, -1]
# arr=[-3, 1, 2, -3, 4, 0]
prefix_sum_map = {}
result = []
cumulative_sum = 0
   
for i in range(len(arr)):
    cumulative_sum += arr[i]
    if cumulative_sum == 0:
        result.append((0, i))
    if cumulative_sum in prefix_sum_map:
        for start_index in prefix_sum_map[cumulative_sum]:
            result.append((start_index + 1, i))        
    if cumulative_sum in prefix_sum_map:
        prefix_sum_map[cumulative_sum].append(i)
    else:
        prefix_sum_map[cumulative_sum] = [i]
print(result)