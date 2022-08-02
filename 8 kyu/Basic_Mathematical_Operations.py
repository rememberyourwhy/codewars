"""Your task is to create a function that does four basic mathematical operations.

The function should take three arguments - operation(string/char), value1(number), value2(number).
The function should return result of numbers after applying the chosen operation.

Examples(Operator, value1, value2) --> output
('+', 4, 7) --> 11
('-', 15, 18) --> -3
('*', 5, 5) --> 25
('/', 49, 7) --> 7"""
# def basic_op(operator, value1, value2):
#     if operator == "+":
#         return value1 + value2
#     elif operator == "-":
#         return value1 - value2
#     elif operator == "*":
#         return value1 * value2
#     else:
#         return value1 / value2
#one line using dictionary
#The day i became a one-liner
def basic_op(operator, a, b):
    return {"+" : a + b, "-" : a - b, "*" : a * b, "/" : a / b if b != 0 else "Not good boi"}[operator]

print(basic_op("/", 1, 0))
