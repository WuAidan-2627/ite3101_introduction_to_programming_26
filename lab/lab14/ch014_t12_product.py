from typing import List

def count (seq:List[int], item:int)->List[int]:
    result=0
    for i in seq:
        if i == item:
            result+=1
    return result