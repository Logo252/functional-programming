import functools

my_list = [1, 2, 3, 4]

sum_of_list = functools.reduce(lambda x, y: x + y, my_list)
print(sum_of_list)
