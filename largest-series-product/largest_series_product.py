import operator
import functools


def largest_product(series: str, size: int) -> int:
    if size < 0 or len(series) < size:
        raise ValueError('Length is less than one or larger than series length')
    if size < 1:
        return 1

    string_length = len(series) - size + 1

    result = [series[i:size+i] for i in range(0, string_length)]
    digits = list(map(list, result))

    max_value = 0
    for digitsList in digits:
        value = functools.reduce(operator.mul, list(map(int, digitsList)))

        if value > max_value:
            max_value = value

    return max_value
