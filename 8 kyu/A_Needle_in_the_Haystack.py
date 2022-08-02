#https://www.codewars.com/kata/56676e8fabd2d1ff3000000c/train/python
"""Can you find the needle in the haystack?

Write a function findNeedle() that takes an array full of junk but containing one "needle"

After your function finds the needle it should return a message (as a string) that says:

"found the needle at position " plus the index it found the needle, so:

Example(Input --> Output)

["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] --> "found the needle at position 5" """

def find_needle(arr, index = 0):
    if arr[index] != "needle":
        return find_needle(arr, index + 1)
    return f"found the needle at position {index}"
arr = ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]
print(find_needle(arr))
