#first approach:

def pick_peaks1(arr):
    """ Treat every element as a peak and check """
    pos = []
    peaks = []

    for i in range(1, len(arr) - 1):
        if check(arr, i) == True:
            pos.append(i)
            peaks.append(arr[i])
    return {"pos": pos, "peaks": peaks}


def check(arr, i):
    # not peak
    if arr[i] <= arr[i - 1] or arr[i] < arr[i + 1]:
        return False
    # peak
    elif arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
        return True
    # not know yet
    #
    r = i + 1
    while r <= len(arr) - 2 and arr[r] == arr[i]:
        r += 1
    if arr[i] > arr[r]:
        return True
    else:
        return False

#second approach
def pick_peaks2(arr):
    start = 0
    run = False
    pos = []
    peaks = []

    for end in range(1, len(arr)):
        if not run:
            if arr[end] <= arr[start]:
                start = end
            else: # arr[end] > arr[start]:
                run = True
                peak = end
        else:
            if arr[end] < arr[peak]:
                pos.append(peak)
                peaks.append(arr[peak])
                run = False
                start = end
            elif arr[end] == arr[peak]:
                continue
            else: # arr[end] > arr[peak]:
                peak = end
    return {"pos": pos, "peaks": peaks}


#print(pick_peaks2([1, 2, 3, 6, 4, 1, 2, 3, 2, 1]))

print(pick_peaks2([3,2,3,6,4,1,2,3,2,1,2,2,2,1]))
print(pick_peaks2([2,1,3,1,2,2,2,2,1]))
#todo: copy this code
def pick_peaks(arr):
    pos = []
    prob_peak = False
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            prob_peak = i
        elif arr[i] < arr[i-1] and prob_peak:
            pos.append(prob_peak)
            prob_peak = False
    return {'pos':pos, 'peaks':[arr[i] for i in pos]}
#todo: explain this code
def pick_peaks(arr):
    peak, pos = [], []
    res = {"peaks": [], "pos": []}

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            peak, pos = [arr[i]], [i]

        elif arr[i] < arr[i - 1]:
            res["peaks"] += peak
            res["pos"] += pos
            peak, pos = [], []

    return res
