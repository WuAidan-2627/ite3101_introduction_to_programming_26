from typing import List

def count (seq:List[int])->List[int]:
    result=[]
    for item in seq:
        if item %2 == 0:
            result.append(item)
    return result