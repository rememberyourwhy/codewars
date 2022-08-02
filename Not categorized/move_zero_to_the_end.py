"""

read list
if not 0. add to the end of new list
else -> count

after finish read through the list
add 0s to the end

"""

def check(num):
    if num == 0:
        return False
    else:
        return True

def move_zero_to_the_end(arr):
    new_arr = list()
    zeros = 0
    for i in arr:
        if check(i):
            new_arr.append(i)
        else:
            zeros += 1
    for i in range(zeros):
        new_arr.append(0)
    return new_arr

print(move_zero_to_the_end([1, 0, 3, 0, 5, 6]))

