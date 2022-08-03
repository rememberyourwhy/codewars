def add_binary(a,b):
    return str(bin(a + b))[2:]

print(add_binary(1,1))

# Can also use this solution, formatting your string
# def add_binary(a,b):
#     return '{0:b}'.format(a + b)