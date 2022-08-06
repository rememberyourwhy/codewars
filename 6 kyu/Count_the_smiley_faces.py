# def count_smileys(arr, count = 0):
#     for element in arr:
#         if len(element) == 2:
#             if check(element[0], element[1]):
#                 count += 1
#         else:
#             if check(element[0], element[2], element[1]):
#                 count += 1
#     return count, arr
#     return #the number of valid smiley faces in array/list

# def check(eyes, mouth, nose = None):
#     face_check = {eyes: ":;", mouth: ")D", nose: "-~"}
#     if nose:
#         for key, value in face_check.items():
#             if key not in value:
#                 return False
#         return True
#     else:
#         return True if (eyes in face_check[eyes] and mouth in face_check[mouth]) else False


# def count_smileys(arr, count=0):
#     eyes = [":", ";"]
#     noses = ["", "-", "~"]
#     mouths = [")", "D"]
#     for face in arr:
#         if face[0] in eyes and face[-1] in mouths and (face[1] in noses if len(face) == 3 else True):
#             count += 1
#     return count



# very clever solution here
# not using regex
# also use "-1" index to check mouth is clever instead of me using "2" or "1" index, this "-1" will be true for both
# the last part is (face[1] in noses if len(face) == 3 else True) I should make a t_o_d_o to come back to this
# one line logic boolean
# Todo Come back to this (face[1] in noses if len(face) == 3 else True) part

# one line solution:
# count_smileys=lambda a:sum(s and s[0]in':;'and s[-1]in')D'and s[1:-1]in('','-','~')for s in a)






print(count_smileys([':oD', ':-D', ';D', ':-D', ';D', ';o(', ':D', ':D', ';(', ';-(', ':o(', ':D', ';(', ':(', ';-D']))
