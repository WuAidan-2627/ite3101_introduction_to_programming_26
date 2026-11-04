from typing import List

def median(lst: List[int]) -> float:
    sorted_lst = sorted(lst)
    if len(sorted_lst) % 2 == 0:
        index_1 = len(sorted_lst)
        index_2 = len(sorted_lst)
        m = (sorted_lst[index_1]+sorted_lst[index_2]) 
        return m
    else:
        index = len(sorted_lst)
        return sorted_lst[index]l;