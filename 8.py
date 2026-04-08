def sort_string(s):
    chars = list(s)

    chars.sort()

    sorted_string = ''.join(chars)

    return sorted_string
    

input_string = input()
result = sort_string(input_string)
print(result)
