def manipulate_s(s):
    s_arr = s.split(", ")
    s_arr[0], s_arr[1] = s_arr[1], s_arr[0]
    return ", ".join(s_arr)


while True:
    s = input()
    print(manipulate_s(s))