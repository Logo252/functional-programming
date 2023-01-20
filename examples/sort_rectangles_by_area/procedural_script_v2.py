# Each element is tuple which contains width and height of rectangle
p = [(3, 3), (4, 2), (2, 2), (5, 2), (1, 7)]

new_p = []


def calculate_area(x):
    return x[0] * x[1]


while p:
    minimum = p[0]
    for x in p:
        if calculate_area(x) < calculate_area(minimum):
            minimum = x
    new_p.append(minimum)
    p.remove(minimum)

print(new_p)
