# https://www.codewars.com/kata/5e28ae347036fa001a504bbe

# LOOP AND SAVE
# find the king and other pieces
# save their coordinates and name into a dictionary
# cor_to_pieces
# data structure: { "x, y" : "name" , "x, y" : "name", ...}
# example: { "2, 4" : "rook",... }

# IN_POSITION("""
#   input : piece (str),
#   return : bool
# """
# subtract
# get [x_remainder, y_remainder]

# CHECK IF THERE ARE ANY HINDRANCE ON THEIR WAY TO THE KING
# check piece_to_distance[piece] == [x_remainder, y_remainder]
# and no_hindrance(piece, piece_coordinate = [  ,  ], king_coordinate = [  ,  ]

def loop_and_save(chessboard):
    cor_and_pieces = []
    king_cor = tuple()
    for x in range(8):
        for y in range(8):
            element = chessboard[x][y]
            if element != " " and element != "♔":
                new_piece = (x, y), element
                cor_and_pieces.append(new_piece)
            elif element == "♔":
                king_cor = (x, y)
            else:
                pass
    return cor_and_pieces, king_cor
    # Output will look like this
    # [((3, 2), '♜'), ((6, 3), '♜')]
    # and (3, 4)


def is_potential_check(piece_item, king_coordination):
    piece_coordination, piece_symbol = piece_item
    # subtracted_coordination (sub_cor)
    x = abs(piece_coordination[0] - king_coordination[0])
    y = abs(piece_coordination[1] - king_coordination[1])
    condition_dict = {
        "♟": x == y and x == 1,
        "♜": x == 0 or y == 0,
        "♞": (x == 2 and y == 1) or (x == 1 and y == 2),
        "♝": x == y,
        "♛": x == 0 or y == 0 or x == y
    }
    return condition_dict[piece_symbol]


board = [
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ','♜',' ','♔',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ','♜',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ']
        ]

print(loop_and_save(board))
# return two value
# first [((3, 2), '♜'), ((6, 3), '♜')]
# second (3, 4)

def no_hindrance(cor_piece, cor_king, chessboard):
    x_piece, y_piece = cor_piece
    x_king, y_king = cor_king





