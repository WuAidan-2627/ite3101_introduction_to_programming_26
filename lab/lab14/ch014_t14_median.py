from typing import List

def median(lst: List[int]) -> float:
    sorted_lst = sorted(lst)
    length = len(sorted_lst)
    if length % 2 == 0:
        index_1 = length
        index_2 = length
        m = (sorted_lst[index_1] + sorted_lst[index_2])
    return m

    index = length
    return sorted_lst[index]