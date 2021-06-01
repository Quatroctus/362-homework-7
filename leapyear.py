
def leapyear(year: int):
    return year % 4 == 0 and (year % 100 != 0)
