def valid_solution(board):
    # create valid dict that has 1 for each from 1 - 9
    # create check that has 0 for each from 1 - 9
    # so we can fill these values later, then check
    valid = {}
    check = {}
    for key in range(1, 10):
        valid[key] = 1
        check[key] = 0
    check_blank = check.copy()  # create a protype

    # check row
    try:  # first check will go throughout the board
        for i in board:
            for j in i:
                check[j] += 1
            if check != valid:
                return False
            check = check_blank.copy()
    except:  # then return False if catch an error (meet 0)
        return False
    # check column
    for j in range(0, 9):
        for i in range(0, 9):
            check[board[i][j]] += 1
        if check != valid:
            return False
        check = check_blank.copy()

    # check cell
    start = [0, 0]
    end = [2, 2]
    while True:
        # this for loop check from start degree to end degree
        for i in range(start[0], end[0] + 1):
            for j in range(start[1], end[1] + 1):
                check[board[i][j]] += 1
        if check != valid:
            return False
        check = check_blank.copy()

        # check if the for loop above is the last
        if end == [8, 8]:
            return True

        # raise indexs after finish filling values and check
        if end[1] != 8:
            start[1] += 3
            end[1] += 3
        else:  # end[1] == 8, change row, reset column
            start[0], start[1] = start[0] + 3, 0
            end[0], end[1] = end[0] + 3, 2


print(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                                   [6, 7, 2, 1, 9, 5, 3, 4, 8],
                                   [1, 9, 8, 3, 4, 2, 5, 6, 7],
                                   [8, 5, 9, 7, 6, 1, 4, 2, 3],
                                   [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                   [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                   [9, 6, 1, 5, 3, 7, 2, 8, 4],
                                   [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                   [3, 4, 5, 2, 8, 6, 1, 7, 9]]))


print(valid_solution(             [[5, 3, 4, 6, 7, 8, 9, 1, 2],
                                   [6, 7, 2, 1, 9, 0, 3, 4, 9],
                                   [1, 0, 0, 3, 4, 2, 5, 6, 0],
                                   [8, 5, 9, 7, 6, 1, 0, 2, 0],
                                   [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                   [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                   [9, 0, 1, 5, 3, 7, 2, 1, 4],
                                   [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                   [3, 0, 0, 4, 8, 1, 1, 7, 9]]))
#todo: check solution of others
"""
def validSolution(board):
    boxes = validate_boxes(board)
    cols = validate_cols(board)
    rows = validate_rows(board)
    return boxes and cols and rows

def validate_boxes(board):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            nums = board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3]
            if not check_one_to_nine(nums):
                return False
    return True

def validate_cols(board):
    transposed = zip(*board)
    for row in transposed:
        if not check_one_to_nine(row):
            return False
    return True
    
def validate_rows(board):
    for row in board:
        if not check_one_to_nine(row):
            return False
    return True
            

def check_one_to_nine(lst):
    check = range(1,10)
    return sorted(lst) == check
"""

"""
def validSolution(board):
    blocks = [[board[x+a][y+b] for a in (0, 1, 2) for b in (0, 1, 2)] for x in (0, 3, 6) for y in (0, 3, 6)]
    return not any(set(x) != set(range(1, 10)) for x in board + list(zip(*board)) + blocks)

#last line: return all(set(x) == set(range(1, 10)) for x in board + list(zip(*board)) + blocks)


"""

"""
from itertools import product

def validSolution(board):
    rows = board
    columns = map(list, zip(*board))
    blocks = [[board[i][j] for (i, j) in product(xrange(x, x+3), xrange(y, y+3))] for (x, y) in product((0, 3, 6), repeat=2)]
    
    return all(sorted(line) == range(1, 10) for lines in (rows, columns, blocks) for line in lines)

"""

"""
import numpy as np
from itertools import chain

nums = set(range(1, 10))

def validSolution(board):
    a = np.array(board)
    r = range(0, 9, 3)
    return all(set(v.flatten()) == nums for v in chain(a, a.T, (a[i:i+3, j:j+3] for i in r for j in r)))

"""

"""
def validSolution(board):
    for x in range(9):
        arr = [board[y][x] for y in range(9)]
        arr2 = [board[x][y] for y in range(9)]
        arr3 = [board[i][y] for y in range(((x%3)*3),(((x%3)*3)+3)) for i in range((int(x/3)*3),(int(x/3)*3)+3)]
        for i in range(9):
            if arr[i] in arr[(i+1):]: return False
            if arr2[i] in arr2[(i+1):]: return False
            if arr3[i] in arr3[(i+1):]: return False
    return True

"""

"""
from itertools import chain

def validSolution(board):
    cols = zip(*board)
    squares = (chain(*(board[y+i][x:x+3] for i in range(3)))
               for x in (0, 3, 6) for y in (0, 3, 6))
    good_range = set(range(1, 10))
    return all(set(zone) == good_range for zone in chain(board, cols, squares))

"""

"""
def validSolution(board):
    correct = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # check rows
    for row in board:
        if sorted(row) != correct:
            return False

    for column in zip(*board):
        if sorted(column) != correct:
            return False

# check regions
    for i in range(3):
        for j in range(3):
            region = []
            for line in board[i*3:(i+1)*3]:
                region += line[j*3:(j+1)*3]
            if sorted(region) != correct:
                return False
# if everything correct
    return True

"""


"""
def valid_solution(a):
    try:
        c=[[a[x][i]for x in range(9)if a[x][i] in range(1,10)]for i in range(9)]
        e=[i for i in a]
        f=[[a[x+n][i+m]for i in range(3)for x in range(3)]for m in range(0,9,3)for n in range(0,9,3)]
        return all([len(set(i))==9for i in c+e+f])
    except:
        return False

"""

"""
def validSolution(board):
    column_list = []
    box_list = []
    column_list.extend([[board[x][y] for x in range(9)] for y in range(9)])
    box_list.extend([board[x][y:y+3] + board[x+1][y:y+3] + board[x+2][y:y+3] for y in range(0,9,3) for x in range(0,9,3)])
    for i in range(1,10):
        for row in board:
            if row.count(i) > 1:
                return False
        for col in column_list:
            if col.count(i) > 1:
                return False
        for bx in box_list:
            if bx.count(i) > 1:
                return False

    return True

"""

"""
def validSolution(board):
    return set(reduce(lambda x,y:x+y,board))==set(range(1,10)) and \
            all(len(set(x))==9 for x in board) and \
            all(len(set(x))==9 for x in map(list,zip(*board))) and \
            all(len(set(board[i/3*3][i%3*3:i%3*3+3]+board[i/3*3+1][i%3*3:i%3*3+3]+board[i/3*3+2][i%3*3:i%3*3+3]))==9 for i in range(0,9))

"""

"""
r03, r09, r093 = range(0, 3), range(0, 9), range(0, 9, 3)
sets = (
    [[(r, c) for c in r09] for r in r09] +
    [[(r, c) for r in r09] for c in r09] +
    [[(r0 + r, c0 + c) for c in r03 for r in r03] for r0 in r093 for c0 in r093]
    )
sum19 = sum(range(1, 10))

def validSolution(board):
    return all(sum(board[r][c] for (r, c) in s) == sum19 for s in sets)
"""


"""
def validSolution(board):
    return (all(len(set(row)) == 9 for row in board)
        and all(len(set(column)) == 9 for column in zip(*board))
        and all(len(set(sum((board[i+k][j:j+3] for k in range(3)), []))) == 9 for i in range(0, 9, 3) for j in range(0, 9, 3)))
"""

