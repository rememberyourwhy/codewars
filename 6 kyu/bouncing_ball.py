# A mathy solution

# The height of the ball after bouncing can be expressed as an exponential function:
#
# f(x) = h * bounce^x
# f(x) is the height the ball reaches after x bounces
# h is initial height
# bounce is the decay factor
#
# By solving the equation f(x) = window, we get the number of
# bounces that will finally put the ball at the exact window height.
#
# Example:
# f(x) = 3 * 0.66^x
# f(x) = 1.5  -->  x ~= 1.67
# So the first bounce will put the ball a bit above window height,
# but the second will put it a bit below.
# This means the ball will pass the window 2 times (one bounce).
#
# If a bounce puts the ball at the exact window height (an exact
# number of bounces, x is an integer), this would mean the ball
# won't pass the window, only appear in front of it.
# However, due to the restriction in this assignment, the ball
# can only be seen if it's height is _strictly_ greater than the
# window height.

import math

def bouncingBall(h, bounce, window):
    # If parameters don't fulfil conditions, return -1
    if not (h > 0 and 0 < bounce < 1 and window < h):
        return -1
    # Solve equation for f(x) = window, using logarithms
    bounces = math.log(window / h, bounce)
    # Get actual number of bounces that still puts the ball above window height
    exactBounces = math.floor(bounces)
    # If last bounce is not strictly higher than window height, it can't be seen
    if bounces == exactBounces:
        exactBounces -= 1
    # The ball will pass the window two times for each bounce, up and down,
    # plus one for the initial drop past window, before first bounce
    passes = exactBounces * 2 + 1
    return passes


#My solution
# def bouncing_ball(h, bounce, window, run=False, count=0):
#     # bro i can feel that some math genius will O(1) this
#     # special condition
#     if h > 0 and bounce > 0 and bounce < 1 and window < h:
#         run = True
#     elif run:
#         pass
#     else:
#         return -1
#     h_next = h * bounce
#     if h > window and h_next > window:
#         count += 2
#     elif h > window:
#         count += 1
#         return count
#     else:
#         return count
#
#     return bouncing_ball(h_next, bounce, window, run, count)