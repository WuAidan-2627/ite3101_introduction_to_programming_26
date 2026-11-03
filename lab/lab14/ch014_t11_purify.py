def purify (seq:List[int])->List[int]:
    result=[]
    for item in seq:
        for item %2 == 0:
            result.append(item)
        return