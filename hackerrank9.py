def diagonal_difference(arr):
    n = len(arr)
    left_sum = 0
    right_sum = 0
    for i in range(n):
        left_sum += arr[i][i]
        right_sum += arr[i][n-i-1]
    return abs(left_sum - right_sum)


arr = [[1,2,3],
       [2,3,4],
       [5,6,7]]
print(diagonal_difference(arr))