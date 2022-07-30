def maxsubArray(arr):
    maxSum = arr[0]
    curSum = 0
    for i in arr:
        if curSum < 0:
            curSum = 0
        curSum += i
        maxSum = max(maxSum, curSum)
    return maxSum

print(maxsubArray([1, -2, 3, 5, -4, 6]))
