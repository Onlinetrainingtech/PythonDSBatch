import collections
d=collections.deque(range(6))
print("Normal deque",d)
d.rotate(2)
print("Right Rotation:",d)
d1=collections.deque(range(6))
d1.rotate(-3)
print('Left Rotation',d1)
