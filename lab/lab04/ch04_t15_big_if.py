# Complete the if and elif statements!
def grade_converter(answer: int) -> str:
    if 90 <= answer:
        return "A"
    elif (80 <= answer) and  (answer< 90):
        return "B"
    elif (70 <= answer) and  (answer< 80):
        return "C"
    elif (65 <= answer) and  (answer< 70):
        return "D"
    else:
        return "F"


# This should print an "A"
print(grade_converter(92))

# This should print a "C"
print(grade_converter(70))

# This should print an "F"
print(grade_converter(61))
