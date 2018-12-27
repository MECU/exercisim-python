def is_leap_year(year: int) -> bool:
    if year.__mod__(4) == 0:
        if year.__mod__(100) == 0:
            if year.__mod__(400) == 0:
                return True
            return False
        return True

    return False
