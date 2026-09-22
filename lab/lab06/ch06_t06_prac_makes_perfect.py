def cube(number: int) -> int:
    return number**3


def by_three(number: int) -> int:
    return cube(number: int) % 3 == 0
