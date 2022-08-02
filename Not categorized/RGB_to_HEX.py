def main(n1, n2, n3):
    return f"{str(change(n1))}{str(change(n2))}{str(change(n3))}"

def change(num):
    if num >= 0 and num <= 255:
        return f"{str(more_hex_values(num // 16 % 16))}{str(more_hex_values(num % 16))}"
    elif num < 0:
        return "{:02d}".format(0)
    elif num > 255:
        return "FF"

def more_hex_values(mod_num):
    if mod_num >= 0 and mod_num <= 9:
        return mod_num
    else:
        match mod_num:
            case 10:
                return A
            case 11:
                return B
            case 12:
                return C
            case 13:
                return D
            case 14:
                return E
            case 15:
                return F

print(main(100, 100, 256))

"""
def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))
"""

#learn using max min combination to round values of our variables
#the use of lambda function here is beautiful too
#02X is built-in format for 2 digit hexadecimal number. kinda like 02d but for heximal
# * 3 for a formating is great thing to do too