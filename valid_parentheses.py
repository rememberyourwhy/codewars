"""
check at each point of the string. the number of open is <= close

at the end of the string. check if the number of open and close is even
"""

def check(s):
    open = 0
    close = 0
    i = 0
    while open >= close and i <= len(s) - 1:
        if s[i] == "(":
            open += 1
        else:
            close += 1
        i += 1

    if open == close and i == len(s):
        return True
    else:
        return False

print(check("(())((()())())"))
print(check(")(())))"))