# def increment_string(strng):
#     number_digits = "0123456789"
#     index = len(strng) - 1
#     if strng == "":
#         return "1"
#     elif strng[index] not in number_digits:
#         return strng + "1"
#
#     while strng[index] in "0123456789":
#         index -= 1
#     index += 1
#     index_all_0 = int(index)
#     while strng[index_all_0] == "0" and index_all_0 < len(strng) - 1:
#         index_all_0 += 1
#
#     start_string = strng[:index_all_0]
#     end_string_part_1 = strng[index_all_0:index]
#     end_string_part_2 = strng[index:]
#     end_int_part_2 = int(end_string_part_2)
#     end_string_increased = end_string_part_1 + str(end_int_part_2 + 1)
#     return start_string + end_string_increased

# Wrong approach and too complicated logic
# Proof:
# Try this test:
#         test.assert_equals(increment_string("foobar099"), "foobar100")
# expected result = "foobar100"
# result = "foobar0100"

# Second approach to this:
# make a function that will increase the end number and if it reach 10 -> turn it to 0
# add 1 to the number above it later


def add_1_to_digit(digit):
    return str(int(digit) + 1)


def increase_num_end(strng_end):
    remain = 1
    result_string = str(strng_end)
    index = len(result_string) - 1
    while remain != 0 and index >= 0:
        added_1 = add_1_to_digit(result_string[index])
        remain = 0
        if added_1 == "10":
            added_1 = "0"
            remain = 1
        result_string = result_string[:index] + added_1 + result_string[index + 1:]
        index -= 1
    if remain == 1:
        result_string = "1" + result_string
    remain = 0
    return result_string


def increment_string(strng):
    number_digits = "0123456789"
    index = len(strng) - 1
    if strng == "":
        return "1"
    elif strng[index] not in number_digits:
        return strng + "1"

    while strng[index] in "0123456789" and index >= 0:
        index -= 1
    index += 1
    increased_end = increase_num_end(strng[index:])
    no_digits_part = strng[:index]
    result_string = no_digits_part + increased_end
    return result_string


result = increment_string('foobar99')
print(result)

# https://www.codewars.com/kata/54a91a4883a7de5d7800009c/solutions/python

# Hey bro, go learn regex