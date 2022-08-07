# import string


# def high(s):
#     # 1 turn input string to a split list
#     s_lower_split = s.lower().split()
#     # 2 get "a-z" string from string module
#     az_lower = string.ascii_lowercase
#     letter_l = []
#     # 3 turn it to a list
#     for i in az_lower:
#         letter_l.append(i)
#     # 4 make score list using list comprehension
#     score_l = [x + 1 for x in range(len(letter_l))]
#
#     # 5 make a dictionary for easy look up
#     letter_to_score = {letter_l[i]: score_l[i] for i in range(len(letter_l))}
#
#     # 6 start looping through list of words
#     highest_index = 0
#     highest_score = 0
#     for index in range(len(s_lower_split)):
#         score = sum(letter_to_score[letter] for letter in s_lower_split[index])
#         if score > highest_score:
#             highest_score = score
#             highest_index = index
#
#     # return word with the highest score from original string
#     return s.split()[highest_index]

# Comment:
# 2 and 3 can be turned into one step (23)
# 23 and 4, 5 can also be turned into one line
# 6 can be turned into one line using recursion

def high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))

def test_max():
    arr = [11, 22, 21, 13, 44]
    return max(arr, key = lambda k: sum(int(str(c) for c in k))

test_max()