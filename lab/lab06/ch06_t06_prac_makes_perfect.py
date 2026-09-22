def cube(number: int) -> int:
    return number**3


def by_three(number2: int) -> int:
    if cube(number2) % 3 == 0:
        return
    else: 
