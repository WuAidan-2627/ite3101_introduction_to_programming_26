def cube(number: int) -> int:
    return number**3


def by_three(number: int) -> int:
    if cube(number) % 3 == 0:
        return cube(number)
    elif cube(number) % 3 != 0:
        return print("False")
