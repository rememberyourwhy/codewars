def unique_in_order(iterable):
    result = []
    pre = None
    for index in range(0, len(iterable)):
        if iterable[index] != pre:
            result.append(iterable[index])
            pre = iterable[index]
    return result

print(unique_in_order('AAAABBBCCDAABBB'))

def unique_in_order(iterable):
    r = []
    for x in iterable:
        x in r[-1:] or r.append(x)
    return r
# Blind4Basics
# it's an "abuse" of the boolean shortcut:
#
# check if x in r[-1:], if so, the or condition is fulfilled so the second statement isn't executed
# if x is not in the end part, the second statement is checked and x is appended to the r list.
# Note that the or condition returns a boolean, but this one isn't used.