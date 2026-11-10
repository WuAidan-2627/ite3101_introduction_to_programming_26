from typing import List

n = [3, 5, 7]


def double_list(n: List[int]) -> List[int]:
    for i in range(0, len(n)):
        n[i] = n[i] * 2
        return n
# Don't forget to return your new list!
def double_list(n: List[int]) -> List[int]:
    for i in range(0, len(n)):
        n[i] = n[i] * 2
        return n


print(double_list(n))
