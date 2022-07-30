#while j < len
#if check:
    #change exist[i] and exist[j] to 0
    #while exist[i] == 0 and i > 0:
        #i -= 1
    #while exist[j] == 0 and j < len(directions) - 1:
    #j += 1
#if (i == 0 and exist[i] == 0) or not check:
    #i = j
    #j = i + 1

def check(dir, exist, i, j):
    pair = {
        "NORTH" : "SOUTH",
        "SOUTH" : "NORTH",
        "EAST"  : "WEST",
        "WEST"  : "EAST"
    }
    if dir[j] == pair.get(dir[i]) and exist[i] and exist[j]:
        return True
    else:
        return False

def directions_reduction(dir):
    exist = [1 for i in range(len(dir))]
    i = 0
    j = 1
    while j < len(dir):
        if check(dir, exist, i, j):
            exist[i] = 0
            exist[j] = 0
            while exist[i] == 0 and i > 0:
                i -= 1
            while exist[j] == 0 and j < len(dir) - 1:
                j += 1
        else:
            i = j
            j = i + 1
        if i == 0 and exist[i] == 0:
            i = j
            j = i + 1
    result = list()
    for k in range(len(exist)):
        if exist[k]:
            result.append(dir[k])
    return result

print(directions_reduction(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))

