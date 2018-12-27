def slices(series: str, length: int) -> list:
    if length < 1 or len(series) < length:
        raise ValueError('Length is less than one or larger than series length')

    result = []
    stringLength = len(series)
    for i in range(0, stringLength - length + 1):
        result.append(series[i:length + i])

    return result
