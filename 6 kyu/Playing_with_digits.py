def dig_pow(n, p):
    # your code
    return get_k(n, get_sum(n, p))


def get_sum(n, p):
    sum = 0
    n_string = str(n)
    for element in n_string:
        sum += int(element) ** p
        p += 1
    return sum

def get_k(n, sum):
    if sum % n == 0:
        k = sum // n
        return k
    else:
        return -1

print(dig_pow(695, 2))