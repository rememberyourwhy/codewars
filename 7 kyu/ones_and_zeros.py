
# def ones_and_zeros(arr, result = 0, power = 0, index = -1):
#     if index >= - len(arr):
#         return ones_and_zeros(arr, result + (2 ** power * arr[index]) , power + 1, index - 1)
#     return result
# print(ones_and_zeros([1, 1, 1, 1]))

#Bro, when u think yourself that you are good
#The truth is:

def binary_array_to_number(arr):
    return int("".join(map(str, arr)), 2)

#FRICKING ONE LINE AND EaSy tO ReAd

#Sample Test
#print(binary_array_to_number([1, 1, 1, 1]))

