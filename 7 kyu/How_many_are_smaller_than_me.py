def binary_search(arr, val, start, end):
    # we need to distinguish whether we should insert
    # before or after the left boundary.
    # imagine [0] is the last step of the binary search
    # and we need to decide where to insert -1
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start + 1

    # this occurs if we are moving beyond left\'s boundary
    # meaning the left boundary is the least position to
    # find a number greater than val
    if start > end:
        return start

    mid = (start + end) // 2
    if arr[mid] < val:
        return binary_search(arr, val, mid + 1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid - 1)
    else:
        return mid


def check_dup(arr, val, mid):
    result = mid
    if arr.count(val) > 1:
        while arr[result] == val and result > 0:
            result -= 1
        if result == 0 and arr[result] == val:
            return result
        else:
            return result + 1
    return result


def insert_sorted(arr, val, index):
    arr.insert(index, val)
    return arr


# loop from the end of the array back to the first element
# with each element,
# binary search it to get insert index
# append check_dup() to its result list
# return the result list

def smaller(arr):
    result_arr = []
    sorted_arr = []
    for index in range(len(arr) - 1, -1, -1):
        element = arr[index]
        insert_index = binary_search(sorted_arr, element, 0, len(sorted_arr) - 1)
        sorted_arr = insert_sorted(sorted_arr, element, insert_index)
        insert_index = check_dup(sorted_arr, element, insert_index)
        result_arr.append(insert_index)

    return result_arr[::-1]


print(smaller([5, 4, 7, 9, 2, 4, 4, 5, 6]))
