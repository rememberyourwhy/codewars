import math
#floor not actually needed here, can use int() instead
def nb_year(p0, percent, aug, p):
    percentage = percent / 100
    p_now = p0
    year = 0
    #p_next =
        #p_now + p_now * percentage + aug
    while p_now < p:
        p_now = p_now + math.floor(p_now * percentage) + aug
        year += 1
    return year

print(nb_year(1000, 2.0, 50, 1214))
#solution page:
#there are recursive function and.

#recursion
# def nb_year(p0, percent, aug, p, years = 0):
#     if p0 < p:
#         return nb_year(p0 + int(p0 * percent / 100) + aug, percent, aug, p, years + 1)
#     return years