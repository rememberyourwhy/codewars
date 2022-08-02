#there is four directions that are possible:
    #left - right: extract yl(row)
    #top - bottom: extract xh(col)
    #right - left: extract yh(row)
    #bottom - top: extract xl(col)

#so we will run a while loop | condition: x_high != x_low & y_high != y_low
#run through the moving direction. base on the direction, extract the elements from 2D list
#change the value so we wont append the same elements to our result list.

def snail(arr):
    dir_dict = {0: "left - right"
                1: "top - bottom"
                2: "right - left"
                3: "bottom - top"}
    #exclusion condition:
    if arr = [[]]:
        return

    #set high, low values
    x_high = len(arr[0]) - 1
    x_low = 0
    y_high = len(arr) - 1
    y_low = 0

    #direction is == 0 at first: (left - right) first
    dir = 0

    #run a while loop with condition we talked about
    while x_high != x_low and y_high != y_low:
        #left - right
        switch(dir) {
            case 0: #left - right
                for i in
        }
        #change direction after extraction:
        if dir != 3:
            dir += 1
        else:
            dir = 0
