def area(x):
    return x[0] * x[1]


# Each element is tuple which contains width and height of rectangle
p = [(3, 3), (4, 2), (2, 2), (5, 2), (1, 7)]

q = sorted(p, key=area)
print(q)