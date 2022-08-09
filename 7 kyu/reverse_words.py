# def reverse_words(text):
#     result = text
#     left = None
#     right = None
#     for index in range(len(text)):
#         character = text[index]
#         if left is None and character != " ":
#             left = index
#         elif left is not None and character == " ":
#             right = index
#             r_word = result[left: right][::-1]
#             result = result[:left] + r_word + result[right:]
#             left = None
#             right = None
#         elif left is not None and index == len(text) - 1:
#             right = index
#             r_word = result[left: right + 1][::-1]
#             result = result[:left] + r_word
#         else:
#             pass
#     return result

# This first solution approach: iterate through the text, find word.
# After finding a word, reverse it.
# Set new result text value

# Second approach:

one = 'A stitch in time saves nothing'.split(' ')
two = 'A stitch in time saves nothing'.split()
print(one)
print(two)
print(one == two)
