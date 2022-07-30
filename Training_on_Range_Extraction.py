def solution(args):
    start, end = 0, 0
    count = 1
    result = []
    for i in range(1, len(args)):
        if args[i] - 1 == args[i - 1]:
            count += 1
            end = i
        if args[i] - 1 != args[i - 1] or i == len(args) - 1:
            if count == 1:
                result.append(str(args[start]))
            elif count == 2:
                result.append(str(args[start]))
                result.append(str(args[end]))
            elif count >= 3:
                result.append(str(args[start]) + "-" + str(args[end]))
            count = 1
            start = i
            end = i
    if args[-1] - 1 != args[-2]:
        result.append(str(args[-1]))
    return ",".join(result)
#What did i learn from this
    #if my code only execute to the index [i - 1]
        #I can add one more element to my list so my last element (len(args))
            #will get executed
# todo: write code for this in the evening

