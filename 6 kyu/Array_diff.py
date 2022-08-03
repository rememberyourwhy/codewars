# def array_diff(a, b):
#     result = list()
#     b_set = set(b)
#     for element in a:
#         if element not in b_set:
#             result.append(element)
#     return result

# Now awake your inner one liner

def array_diff(a, b, index = 0, result = []):
    if index < len(a):
        if a[index] not in set(b):
            print(a[index])
            return array_diff(a, b, index + 1, result.append(a[index]))
        else:
            return array_diff(a, b, index + 1, result)
    return result

print(array_diff([1,2], [1]))