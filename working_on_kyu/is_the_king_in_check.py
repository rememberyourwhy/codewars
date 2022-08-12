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
    cor_to_pieces = {}
    for x in range(8):
        for y in range(8):
            element = chessboard[x][y]
            if element != " " and element != "♔":
                cor_to_pieces[f"{x}, {y}"] = element
            elif element == "♔":
                king_cor = f"{x}, {y}"
            else:
                pass
    return cor_to_pieces, king_cor


board = [
            [' ',' ',' ',' ',' ',' ',' ','♝'],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            ['♔',' ',' ',' ',' ',' ',' ',' ']
        ]
print(loop_and_save(board))

