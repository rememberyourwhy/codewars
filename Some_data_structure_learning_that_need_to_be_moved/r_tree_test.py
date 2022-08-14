from rtree import index

idx = index.Index()
"""
id (int) – A long integer that is the identifier for this index entry. 
IDs need not be unique to be inserted into the index, 
and it is up to the user to ensure they are unique if this is a requirement.

coordinates (Any) – This may be an object that satisfies the numpy array
protocol, providing the index’s dimension * 2 coordinate pairs 
representing the mink and maxk coordinates in each dimension 
defining the bounds of the query window. For a TPR-Tree, 
this must be a 3-element sequence 
including not only the positional coordinate pairs 
but also the velocity pairs minvk and maxvk and a time value as a float.

obj (Optional[object]) – a pickleable object. If not None, this object will be stored in the index with the id.

"""
# Example code:
idx.insert(0, (30, 20, 30, 20))
idx.insert(0, (30, 15, 30, 15))
idx.insert(0, (30, 16, 30, 16))
idx.insert(0, (30, 26, 30, 26))
idx.insert(1, (30, 36, 30, 36))
hits = idx.nearest((30, 31, 30, 31), 1, objects=True)
for i in hits:
    print(i.id)
    print(i.bbox)

# Index.insert require 3 parameters.
# First: ID. This can be anything, not important, someone should change it. So it has default value of 0 or something.
# Second: Coordinates of the object. I think this requires a box coordinate mean there are 2 pairs of x, y coordinates.
# Third: also can be anything. which is very weird we have two parameters that do the same thing.
# Both is for "marking" the object.
# So ill work with just two first parameter of insert method.
# ID and coordinates.
# Process of making and doing NNS will look something like this
# idx.insert(id = 0, (x1, y1, x2, y2))
# idx.insert(id = 1, (x1, y1, x2, y2))
# idx.insert(id = 2, (x1, y1, x2, y2))
# idx.insert(id = 3, (x1, y1, x2, y2))
# idx.insert(id = 4, (x1, y1, x2, y2))
# hits = idx.nearest((0, 0, 0, 0), 1, objects=True)
# for i in hits:
#     print(i.id)
#     print(i.bbox)
# With the example above I think we are done with most uses of this package
# That is to find the nearest coordinate from a list toward an input point
