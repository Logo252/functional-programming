def reverse_string(string_to_reverse):
    reversed_string = []
    index = len(string_to_reverse)

    while index > 0:
        reversed_string += string_to_reverse[index - 1]
        index = index - 1

    return ''.join(reversed_string)


_input = input("Enter your string: ")
print('Reversed string: ', reverse_string(_input))
