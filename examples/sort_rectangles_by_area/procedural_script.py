# Each element is tuple which contains width and height of rectangle
p = [(3, 3), (4, 2), (2, 2), (5, 2), (1, 7)]


# ???

def calculate_area(x):
    return x[0] * x[1]


def add_to_dict():
    new_dict = {}
    for element in p:
        area = calculate_area(element)
        new_dict.update({element: area})

    return new_dict


def sort():
    new_dict = add_to_dict()
    dict_output = {}
    for key, value, item in new_dict.items():
        minimum = value
        for key_2, value_2 in new_dict.items() - item:
            if value > value_2:
                temp = value
                value = value_2
                value_2 = temp

                # dict_output.update({key_2: value_2})
                # new_dict.pop(key_2)

    return dict_output.keys()


result = list(sort())
print()

# dict key p(3,3), value sum
# sortint sumas value
# du forai
# paverst  i key values

# print(dict)


# sort()

# dict_Test = {(3, 3): 9, (4, 2): 8, (2, 2): 4, (5, 2): 10, (1, 7): 7}
