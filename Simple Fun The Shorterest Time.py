#problem link on codewars
#https://www.codewars.com/kata/5953c6f8af7ac14fd4000021/train/javascript
import math

def shorterestTime(n,m,speeds):
    a, b, c, d = [element for element in speeds]
    if n == 0:
        return 0

    walk_only = t1 =  d * n
    walk_to_elavator = t2 = (d * abs(m - n)) + (a * m) + (2 * b) + c
    wait_elevator = t3 = (a * abs(m - n)) + (a * n) + (2 * b) + c
    return min(t1, t2, t3)

print(shorterestTime(0,5,[1,2,3,10]))
print(shorterestTime(4,4,[1,2,3,10]),11)
print(shorterestTime(1,1,[1,2,3,10]),8)
print(shorterestTime(1,1,[2,3,4,10]),10)
print(shorterestTime(4,3,[1,2,3,10]),12)
print(shorterestTime(4,3,[2,3,4,5]),20)
print(shorterestTime(7,6,[3,1,1,4]),25)