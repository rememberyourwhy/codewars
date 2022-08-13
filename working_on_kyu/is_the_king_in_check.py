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
        "♟": x == y and x == 1 and piece_coordination[0] - king_coordination[0] < 0,
        "♜": x == 0 or y == 0,
        "♞": (x == 2 and y == 1) or (x == 1 and y == 2),
        "♝": x == y,
        "♛": x == 0 or y == 0 or x == y
    }
    return condition_dict[piece_symbol]


def distance_to_step(distance):
    if distance != 0:
        if distance < 0:
            return -1
        else:
            return 1
    else:
        return 0


def no_hindrance(cor_piece, cor_king, chessboard):
    x_piece, y_piece = cor_piece
    x_king, y_king = cor_king
    x_distance = x_king - x_piece
    y_distance = y_king - y_piece
    x_step = distance_to_step(x_distance)
    y_step = distance_to_step(y_distance)
    x_next = x_piece + x_step
    y_next = y_piece + y_step
    while x_next != x_king or y_next != y_king:
        if chessboard[x_next][y_next] != " ":
            return False
        x_next += x_step
        y_next += y_step
    return True


def king_is_in_check(chessboard):
    # Step 1: save white pieces and black_king coordinates
    # Step 2: check if they are in potential position to check black king
    # Step 3: check if there are hindrances between king and that piece
    # can be rook, bishop or queen
    cor_and_piece_symbol, king_cor = loop_and_save(chessboard)
    for piece in cor_and_piece_symbol:
        # pawn and knight no worry abt hindrance
        if is_potential_check(piece, king_cor) and (piece[1] == "♟" or piece[1] == "♞"):
            return True
        # others do, so we have to check them
        elif is_potential_check(piece, king_cor) and no_hindrance(piece[0], king_cor, chessboard):
            return True
        else:
            pass
    return False

board = [
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ','♔',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ','♜',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ','♜',' ',' ',' ']
        ]
print(no_hindrance((3, 2), (3, 4), board))
print(king_is_in_check(chessboard=board))
