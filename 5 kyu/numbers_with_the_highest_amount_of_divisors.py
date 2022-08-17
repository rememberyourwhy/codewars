# https://www.codewars.com/kata/55ef57064cb8418a3f000061/train/python
# ------------------------ Declare Variables ------------------- #


# ----------------- Problem 1: Return number of integer in arr input -- #
def num_int(arr):
    return len(arr)


# ----------------- Problem 2: Return number of prime number ------- #
def prime_num_check(num):
    for _ in range(2, int(num ** 0.5) + 1):
        if num % _ == 0:
            return False
    return True


def prime_counter(arr):
    count = 0
    for _ in arr:
        if prime_num_check(_):
            count += 1
    return count


# ----------------- Problem 3: Return the highest divisors count ------- #
# ----------------- and the array content these satisfy number in input arr ------- #
def divisors_counter(num):
    """ count number of divisors that a number (num) has"""
    count = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            count += 1
            if i != num // i:
                count += 1
    return count


def highest_amount_divisors(arr):
    max_divisors = 0
    result = []
    for _ in arr:
        current_counter = divisors_counter(_)
        if current_counter > max_divisors:
            max_divisors = current_counter
            result = [_]
        elif current_counter == max_divisors:
            result.append(_)
    return max_divisors, sorted(result)


def proc_arrInt(listNum):
    num_counter = num_int(listNum)
    prime_num_counter = prime_counter(listNum)
    highest_divisors_num = highest_amount_divisors(listNum)
    return [num_counter, prime_num_counter, [highest_divisors_num[0], highest_divisors_num[1]]]





