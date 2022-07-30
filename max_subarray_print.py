def max_subarray(arr):
    maxSum = arr[0]
    curSum = 0
    for i in arr:
        if curSum < 0:
            curSum = 0
        curSum += i
        maxSum = max(curSum, maxSum)
    return maxSum

def printattemp(arr, maxSum):
    curSum = 0
    i = 0
    maxArr = list()
    while curSum != maxSum:
        if curSum < 0:
            curSum = 0
        curSum += arr[i]
        i += 1
    i -= 1
    while curSum:
        curSum -= arr[i]
        maxArr.append(arr[i])
        i -= 1
    return list(reversed(maxArr))

#extension:
def second_max_subarray(arr, maxSum):
    secondSum = arr[0]
    curSum = 0
    for i in arr:
        if curSum < 0:
            curSum = 0
        curSum += i
        if maxSum - curSum:
            secondSum = max(secondSum, curSum)
    return secondSum


arr = [1, 3, -5, 4, 12, -7, 5]
maxSum = max_subarray(arr)
maxArr = printattemp(arr, maxSum)
secondSum = second_max_subarray(arr, maxSum)
print(maxSum)
print(maxArr)
print(secondSum)
