# def tower_builder(n_floors):
#     #mid = "*"
#     #left = " " * (n_floors - now_floor - 1) + "*" * now_floor
#     #right = left[::-1]
#     #str_floor = "".join([left, mid, right])
#     #arr_floor.append(str_floor)
#     arr_floor = []
#     for now_floor in range(n_floors):
#         mid = "*"
#         left = " " * (n_floors - now_floor - 1) + "*" * now_floor
#         right = left[::-1]
#         str_floor = "".join([left, mid, right])
#         arr_floor.append(str_floor)
#     return arr_floor


def tower_builder(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]

# Check out this one line solution

# Solution page = https://www.codewars.com/kata/576757b1df89ecf5bd00073b/solutions/python