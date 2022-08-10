# https://www.codewars.com/kata/5e28ae347036fa001a504bbe

# def king_is_in_check(chessboard):
#     # get the line where both the white piece and black king are on
#     for x in range(8):
#         for y in range(8):
#             if chessboard[x][y] == "♔":
#                 king_x = x
#                 king_y = y
#     for x in range(8):
#         for y in range(8):
#             if chessboard[x][y] != " " and chessboard[x][y] != "♔":
#                 piece_x = x
#                 piece_y = y
#                 line = line_of_active(chessboard, piece_x, piece_y, king_x, king_y)
#                     if chessboard[x][y] == "♞":
#                         return True
#                     if no_hindrance(line):
#                         return True


# def line_of_active(x1, y1, x2, y2):
#     pieces_dict = {
#         "♟": [[x1 - 1, y1 - 1][x1 - 1, y1 + 1][x1 + 1, y1 - 1][x1 + 1, y1 + 1]]
#         "♞": [[x1 - 2, y1 - 1],[x1 - 2, y1 + 1],[x1 + 2, y1 - 1],[x1 + 2, y1 + 1],
#               [x1 - 1, y1 - 2],[x1 - 1, y1 + 2],[x1 + 1, y1 - 2],[x1 + 1, y1 + 2]]
#         "♝": [[x1 - 0, y1 - 0],[x1 - 1, y1 - 1],[x1 - 2, y1 - 2],[x1 - 3, y1 - 3],
#               [x1 - 4, y1 - 4],[x1 - 5, y1 - 5],[x1 - 6, y1 - 6],[x1 - 7, y1 - 7],
#               [x1 + 0, y1 + 0],[x1 + 1, y1 + 1],[x1 + 2, y1 + 2],[x1 + 3, y1 + 3],
#               [x1 + 4, y1 + 4],[x1 + 5, y1 + 5],[x1 + 6, y1 + 6],[x1 + 7, y1 + 7]]
#         "♜": [[x1 + 0, y1],[x1 + 1, y1],[x1 + 2, y1],[x1 + 3, y1],
#               [x1 + 4, y1],[x1 + 5, y1],[x1 + 6, y1],[x1 + 7, y1],
#               [x1 - 0, y1],[x1 - 1, y1],[x1 - 2, y1],[x1 - 3, y1],
#               [x1 - 4, y1],[x1 - 5, y1],[x1 - 6, y1],[x1 - 7, y1],
#               [x1, y1 + 0],[x1, y1 + 1],[x1, y1 + 2],[x1, y1 + 3],
#               [x1, y1 + 4],[x1, y1 + 5],[x1, y1 + 6],[x1, y1 + 7],
#               [x1, y1 - 0],[x1, y1 - 1],[x1, y1 - 2],[x1, y1 - 3],
#               [x1, y1 - 4],[x1, y1 - 5],[x1, y1 - 6],[x1, y1 - 7]]
#         "♛": [[x1 - 0, y1 - 0],[x1 - 1, y1 - 1],[x1 - 2, y1 - 2],[x1 - 3, y1 - 3],
# #               [x1 - 4, y1 - 4],[x1 - 5, y1 - 5],[x1 - 6, y1 - 6],[x1 - 7, y1 - 7],
# #               [x1 + 0, y1 + 0],[x1 + 1, y1 + 1],[x1 + 2, y1 + 2],[x1 + 3, y1 + 3],
# #               [x1 + 4, y1 + 4],[x1 + 5, y1 + 5],[x1 + 6, y1 + 6],[x1 + 7, y1 + 7]],
#                 [x1 + 0, y1],[x1 + 1, y1],[x1 + 2, y1],[x1 + 3, y1],
# #               [x1 + 4, y1],[x1 + 5, y1],[x1 + 6, y1],[x1 + 7, y1],
# #               [x1 - 0, y1],[x1 - 1, y1],[x1 - 2, y1],[x1 - 3, y1],
# #               [x1 - 4, y1],[x1 - 5, y1],[x1 - 6, y1],[x1 - 7, y1],
# #               [x1, y1 + 0],[x1, y1 + 1],[x1, y1 + 2],[x1, y1 + 3],
# #               [x1, y1 + 4],[x1, y1 + 5],[x1, y1 + 6],[x1, y1 + 7],
# #               [x1, y1 - 0],[x1, y1 - 1],[x1, y1 - 2],[x1, y1 - 3],
# #               [x1, y1 - 4],[x1, y1 - 5],[x1, y1 - 6],[x1, y1 - 7]]
#     }
s = ""
for _ in range(8):
    s = s + f"[x1 + {_}, y1],"
for _ in range(8):
    s = s + f"[x1 - {_}, y1],"
for _ in range(8):
    s = s + f"[x1, y1 + {_}],"
for _ in range(8):
    s = s + f"[x1, y1 - {_}],"

print(s)

        # check if there are any hindrance


board = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['♜', ' ', '♝', '♔', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ]

# Todo: Continue doing this
