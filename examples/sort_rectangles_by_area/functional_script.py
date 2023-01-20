def area(x):
    return x[0] * x[1]


def first_element(x):
    return x[0]


# Each element is tuple which contains width and height of rectangle
p = [(3, 3), (4, 2), (2, 2), (5, 2), (1, 7)]

q = sorted(p, key=first_element)
print(q)
