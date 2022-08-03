# My solution
# def find_uniq(arr):
#     count = {}
#     index = 0
#     #Check special condition, always worth if we have time to code this out
#     if arr[0] != arr[1] or arr[1] != arr[2] or arr[0] != arr[2]:
#         for element in arr[0:3]:
#             if arr[0:3].count(element) == 1:
#                 return element
#     else:
#         count[arr[0]] = 1
#     while arr[index] in count:
#         index += 1
#     return arr[index]
#     #Time complexity: O(n)

# While I'll agree that "best practice" isn't necessarily the best tag, I think your critique here is flawed.
#
# This solution is O(n) time complexity in best, average, and worst cases.
# There are solutions that are O(1) in the best case (no solution is better than O(n) in the worst case),
# but whether they are going to be faster or not is largely going to depend on the actual data they receive in theory.
#
# In practice, I've yet to see any solution in pure python that has tested faster than this solution with the exception
# of Blind4Basics' forks of this solution, which do greatly narrow down the second step.
#
# Part of the reason this solution is fast, is because set is a bit of a cheat in that it uses a lot of C code under the hood.
# Assuming your unique number is not within 0.32% of the beginning of the array (a pretty safe bet),
# it's going to be faster than just iterating over the array in python.
#
# That the code is compact is merely a nice bonus.
#
# In any case, I'm vigorously against downvoting.
# Having a meaningful discussion about disagreements (as has happened here, repeatedly, even if people don't always read the other comments) is far more useful for everyone than a -1.
# So to sum it up
def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b
#This solution will be faster than iterate through a list since set() conversion is a "cheat" code in C
