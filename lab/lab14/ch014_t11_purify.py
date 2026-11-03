from typing import List
from unittest impoer result


def purify (seq:List[int])->List[int]:
    result=[]
    for item in seq:
        for item % 2 == 0:
            result.append(item)
        return result