#Recursive function (sum, x, n)
    #Check condition
        #When sum = n --> Return storing list of right result
        #When x reach 0 (mean that the recursive phase go to an end)
            # -->  Refresh the storing list
            # --> Refresh sum
            # Return

    #Recursive part
        #Compare sum and n
        #If right (mean that sum < n)
            #adjust sum value (add xk ^ 2))
            #append the storing list
        #Else:
            #return

    #Iterate part
        #call recursive function with these set of values: (sum, x - 1, n)


#ChecksumFunction
    #get sum (before adding new x ^ 2), x, n
    #check if new sum will be smaller then n:
        #return True
    #Else:
        #return False

#Main Function
#input n from test file
#return result from recursive function

# def decompose(n):
#     result = recursive(0, n - 1, n)
#     result.reverse()
#     return result
#
# def recursive(sum, x, n, result = []):
#     #Check condition
#     if sum == n * n:
#         return result
#     if x == 0:
#         if result != None:
#             x = result.pop(-1)
#         else:
#             return
#         sum -= x * x
#         if x == 0:
#             return None
#         else:
#             return recursive(sum, x - 1, n)
#
#
#     #Recursive part
#     if check_sum_and_n(sum, x, n):
#         sum += x * x
#         result.append(x)
#         return recursive(sum, x - 1, n)
#     else:
#         return recursive(sum, x - 1, n)
#
# def check_sum_and_n(sum, x, n):
#     sum += x * x
#     if sum <= n * n and x != 0:
#         return True
#     else:
#         return False
#
# print(decompose(8))

def decompose(n, a=None):
    if a == None: a = n*n
    if a == 0: return []
    for m in range(min(n-1, int(a ** .5)), 0, -1):
        sub = decompose(m, a - m*m)
        if sub != None: return sub + [m]

#Better solution
#this will work until a == 0 --> sum == n --> we have our first satisfied value
    #then it will recurse back to its root
    #so the result list will naturally increase from bottom to top ( small to big ).
    #clever solution, should be the one they intended to direct solver to do

