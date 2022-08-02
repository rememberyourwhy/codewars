#https://www.codewars.com/kata/52c4dd683bfd3b434c000292/solutions/python

# def followed_by_all_zeros(n):
#     n_string = str(n)
#     if n_string[0] != 0:
#         for element in n_string[1:]:
#             if element != "0":
#                 return False
#         return True
#     else:
#         return False
#
#
# def every_digit_is_the_same_number(n):
#     n_string = str(n)
#     first_character = n_string[0]
#     if n_string.count(first_character) == len(n_string):
#         return True
#     else:
#         return False
#
# print(every_digit_is_the_same_number(111))
# # def sequential_incrementing(n):
# #     n_string = str(n)
# #     increasing_string = "1234567890"
# #     for index in range(0, len(n_string) - 1):
# #         if increasing_string[int(n_string[index])] != n_string[index + 1]:
# #             return False
# #     return True
#
# # Can do one more function for decrementing, but we can merge both of them this way. So its not needed
#
# def sequential(n):
#     n_string = str(n)
#     n_string_reversed = n_string[::-1]
#     increasing_string = "1234567890123456789"
#     if increasing_string.find(n_string) == -1 and increasing_string.find(n_string_reversed) == -1:
#         return False
#     else:
#         return True
#
#
# # result = sequential(6544)
# # print(result)
#
# def palindrome(n):
#     n_string = str(n)
#     left = 0
#     right = len(n_string) - 1
#     while left < right:
#         if n_string[left] != n_string[right]:
#             return False
#         left += 1
#         right -= 1
#     return True
#
#
# def one_of_the_value_in_awesome_phrases(n, arr):
#     if n in arr:
#         return True
#     else:
#         return False
#
#
# def b_to_n(boolean_val):  # boolean_to_number
#     if not boolean_val:
#         return 0
#     else:
#         return 1
#
#
# def check_all_conditions(n, arr):
#     if n < 100:
#         return False
#     sum = b_to_n(followed_by_all_zeros(n)) + b_to_n(every_digit_is_the_same_number(n)) + b_to_n(sequential(n)) + b_to_n(
#         palindrome(n) + b_to_n(one_of_the_value_in_awesome_phrases(n, arr)))
#     if sum > 0:
#         return True
#     else:
#         return False
#
#
# def is_interesting(n, arr):
#     if not (check_all_conditions(n, arr) or check_all_conditions(n + 1, arr) or check_all_conditions(n + 2, arr)):
#         return 0
#     elif check_all_conditions(n, arr):
#         return 2
#     else:
#         return 1
#
# #CAN I BE A ONE LINER
# #BRU

