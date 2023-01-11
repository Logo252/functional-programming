# Each element is tuple which contains width and height of rectangle
p = [(3, 3), (4, 2), (2, 2), (5, 2), (1, 7)]

q = sorted(p, key=lambda x: x[0] * x[1])
print(q)
