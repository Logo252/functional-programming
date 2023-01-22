def remove_duplicates_from_string(_string):
    result = ''
    for char in _string:
        if char not in result:
            result += char
    return result


_input = input("Enter your string: ")
print('String without duplicated chars: ', remove_duplicates_from_string(_input))
