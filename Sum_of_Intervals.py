#Sort intervals function
# two posibility
#
# First:
# Starting value is equal
# Second:
# Starting value is not equal
# with the first one, we will let small end value stand above
#
# def compare_equal(a, b):
#     if a[0] == b[0] and a[1] == b[1]:
#         return True
#     return False
#
# def compare_smaller(a, b):
#     if a[0] < b[0] or ( a[0] == b[0] and a[1] < b[1] ):
#         return True
#     return False
#
# def compare_bigger(a, b):
#     if a[0] > b[0] or ( a[0] == b[0] and a[1] > b[1] ):
#         return True
#     return False

def binary_search(arr, val, start, end):
    #if a[0] is the last step of our binary search, we will have to find pos to put our val this way
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start + 1

    #if start > end mean that left pointer has just changed. <-> binary_search_temp < val
    if start > end:
        return start

    #from now its normal binary search steps
    #change mid
    #check condition:
        #if arr[mid] < val:
            #run binary_search(arr, val, mid + 1, end)
        #else:
            #run binary_search(aar, val, start, mid - 1)
    mid = (start + end) // 2
    if arr[mid] < val:
        return binary_search(arr, val, mid + 1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid - 1)
    else:
        return mid

def binary_sort(arr):
    #iterate from second element (Index one) to the end of the array
    #the left part of i is always sorted
    #save arr[i] as a variable val
    #use binary search to get position (we call it "pos" variable) that just bigger than "val"
    #shift all right elements from pos to i - 1 toward the right
    #simutiously put [val] in before arr["pos"]

    for i in range(1, len(arr)):
        val = arr[i]
        pos = binary_search(arr, val, 0, i - 1)
        arr = arr[:pos] + [val] + arr[pos : i - 1] + arr[i + 1:]
    return arr

#if occur overlapping intervals, turn two temp interval to one
#else: turn temp interval to the new one, then add old interval's length to the sum

def sum_of_interval(arr):
    temp_interval = arr[0]
    sum = 0
    for index in range(1, len(arr)):
        #overlapping intervals
        if temp_interval[1] <= arr[index][0]:
            temp_interval = [temp_interval[0], arr[index][1]]
        else:
            sum += temp_interval[1] - temp_interval[0]
            temp_interval = arr[index]
    sum += temp_interval[1] - temp_interval[0]
    return sum
arr = [
   [1,4],
   [7, 10],
   [3, 5],
   [5, 10]
]
sorted_list = binary_sort(arr)
sum = sum_of_interval(sorted_list)
print(sum)




