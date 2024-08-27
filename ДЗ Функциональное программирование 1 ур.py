int_list = [1, 3, 3, 4, 6, 9]
functions = [max, min, len, sum, sorted]


def apply_all_func(int_list, *functions):
    result = {}
    for function in functions:
        result[function.__name__] = function(int_list)
    return result


result = apply_all_func(int_list, *functions)
print(result)
