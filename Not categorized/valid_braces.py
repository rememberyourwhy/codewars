"""
if find an open brace:
    run the check program

the check program is recusive

if find a closed brances:
    check if its correct one:
        True: return True
        False: return False
"""

"""

d = {
    "(" : ")",
    "[" : "]",
    "{" : "}"
    }

def check(s, start = 0):
    if s[start] not in d.keys():
        return False
    for i in range(start, len(s)):
        if s[i] in d.keys():
            if not check(s, i):
                return False
        elif s[i] not in d.keys():
            if d.get(s[start]) != s[i]:
                return False
            else:
                return
    return True

print(check("(){}[]"))
"""

#Recusive try: failed
#Reason: not having enough with recusion. Cant apply to the solution

#new approach:
#each time seeing an open brace:
    #add its index to a list

#each time seeing a close brace:
    #check the last element in the list (the last open brace)
    #if they are not matched:
        #return False
    #else:
        #remove that open brace index from the list

def check(s):
    open_list = list()
    d = {
        "(" : ")",
        "[" : "]",
        "{" : "}"
    }
    for i in range(len(s)):
        if s[i] in d.keys():
            open_list.append(i)
        else:
            if not open_list or d.get(s[open_list.pop()]) != s[i]:
                return False
    return True

print(check("()"))

#I proud abt this solution
#Short and optimized


"""
"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False
"""