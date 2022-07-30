import math
from operator import itemgetter
import time


class Solution:
    primes = []

    def is_prime(num):
        # global primes

        stopPoint = math.sqrt(num)
        for divisor in Solution.primes:
            if divisor > stopPoint:
                break
            if num % divisor == 0:
                return False
        Solution.primes.append(num)
        return True

    def factorization(num):
        num = abs(num)
        factors = []
        divisor = 2
        while num > 1:
            if Solution.is_prime(divisor):
                if num % divisor == 0:
                    factors.append(divisor)
                    num //= divisor

                else:
                    divisor += 1

            else:
                divisor += 1

        return list(dict.fromkeys(factors))

    def sum_for_list(list):
        dict_result = {}
        result = []
        for element in list:
            factors = Solution.factorization(element)
            for factor in factors:
                if factor in dict_result:
                    dict_result[factor] += element
                else:
                    dict_result[factor] = element

        for key, value in dict_result.items():
            result.append([key, value])
        result = sorted(result, key=itemgetter(0))
        return result
start_time = time.time()
print(Solution.sum_for_list([15, 30, -45]))
print("--- %s seconds ---" % (time.time() - start_time))


#We will work with our prime factorization first
    #def is_prime (num):check if a number is prime

    #def factorization (num):
        #generate numbers: (while our number > 1)
            #check is_prime(num)
            #check if its a factor
                #divide num / factor
                #save result
                #keep doing this till we cant divide anymore

            #else: ( not a prime num or not a factor ):
                #increase
        #return list of result

#todo: code like this, please.
#todo: WTF, runtime error????? :D :D :D
#todo: i should be happy with this by now
#CHECK: https://www.codewars.com/kata/54d496788776e49e6b00052f/discuss/python#6104c3a92c938a003e034d16



"""
import math
from operator import itemgetter

primes = []

def is_prime(num):
    global primes
    
    stopPoint = math.sqrt(num)
    for divisor in primes:
        if divisor > stopPoint:
            break
        if num % divisor == 0:
            return False
    primes.append(num)
    return True

def factorization(num):
    num = abs(num)
    factors = []
    divisor = 2
    while num > 1:
        if is_prime(divisor):
            if num % divisor == 0:
                factors.append(divisor)
                num //= divisor

            else:
                divisor += 1

        else:
            divisor += 1

    return list(dict.fromkeys(factors))

def sum_for_list(list):
    dict_result = {}
    result = []
    for element in list:
        factors = factorization(element)
        for factor in factors:
            if factor in dict_result:
                dict_result[factor] += element
            else:
                dict_result[factor] = element

    for key, value in dict_result.items():
        result.append([key, value])
    result = sorted(result, key=itemgetter(0))
    return result
"""
