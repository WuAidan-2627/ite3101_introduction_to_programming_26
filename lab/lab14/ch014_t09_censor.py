def censor(text: str) -> str:
    result=[]
    for s in text.split():
        result.append("*"*len(word))
        