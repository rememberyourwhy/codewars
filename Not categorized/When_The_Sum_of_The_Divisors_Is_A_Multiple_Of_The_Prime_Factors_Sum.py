#https://www.codewars.com/kata/562c04fc8546d8147b000039/train/python
"""
The numbers 12, 63 and 119 have something in common related with their divisors and their prime factors, let's see it.

Numbers PrimeFactorsSum(pfs)        DivisorsSum(ds)              Is ds divisible by pfs
12         2 + 2 + 3 = 7         1 + 2 + 3 + 4 + 6 + 12 = 28            28 / 7 = 4,  Yes
63         3 + 3 + 7 = 13        1 + 3 + 7 + 9 + 21 + 63 = 104         104 / 13 = 8, Yes
119        7 + 17 = 24           1 + 7 + 17 + 119 = 144                144 / 24 = 6, Yes
There is an obvius property you can see: the sum of the divisors of a number is divisible by the sum of its prime factors.

We need the function ds_multof_pfs() that receives two arguments: nMin and nMax, as a lower and upper limit (inclusives)
, respectively, and outputs a sorted list with the numbers that fulfill the property described above.

We represent the features of the described function:

ds_multof_pfs(nMin, nMax) -----> [n1, n2, ....., nl] # nMin ≤ n1 < n2 < ..< nl ≤ nMax
Let's see some cases:

ds_multof_pfs(10, 100) == [12, 15, 35, 42, 60, 63, 66, 68, 84, 90, 95]

ds_multof_pfs(20, 120) == [35, 42, 60, 63, 66, 68, 84, 90, 95, 110, 114, 119]
Enjoy it!!

"""

#first approach, when checking for divisors, get the value of num // divisor too
#problem with this, if that num// divisor is a prime, and it is larger then stopPoint
    #when divisor reached stop point, num is still not = 1
    #so the loop will be continue

"""
import math
import time


primes_set = set()

def is_Prime(num):
    global primes, primes_set

    #if num in primes_set:
     #   return True
    stopPoint = math.sqrt(num)
    for i in primes_set:
        if i > stopPoint:
            break
        if num % i == 0:
            return False
    primes_set.add(num)
    return True

def check_condition(num):

    divisor = 2
    pfs, ds = 0, num + 1
    num_copy = int(num)
    stopPoint = math.sqrt(num)
    #get pfs
    while num > 1 or divisor < stopPoint :
        while is_Prime(divisor) == True and num % divisor == 0:
            pfs += divisor
            num //= divisor
        if num_copy % divisor == 0:
            ds += divisor
            ds += num_copy // divisor
        divisor += 1
    print(ds,pfs)

    if ds % pfs == 0:
        return True

    else:
        return False

def ds_multof_pfs(nMin, nMax):
    result = []
    for i in range(nMin, nMax + 1):
        if check_condition(i) == True:
            result.append(i)

    return result


start_time = time.time()
print(21 + 6 + 14 + 42 + 1 + 3 + 7 + 2)
print(check_condition(42))
#42 = 3* 7 * 2 ds =
print("--- %s seconds ---" % (time.time() - start_time))
"""