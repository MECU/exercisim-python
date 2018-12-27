def is_armstrong(number: int):
    number_string = number.__str__()
    length = number_string.__len__()

    total = 0
    for x in number_string[::1]:
        total += int(x) ** length

    return number == total
