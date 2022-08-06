"""ATM allow 4 or 6 digit PIN codes and PIN codes cannot contain anything
but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false."""

# One line solution


def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()


# Normal solution
# def validate_pin(pin):
#     if len pin == 4 or len pin == 6:
#         for element in pin:
#             if str(element) not in "1234567890":
#                 return False
#         return True
#     return True
