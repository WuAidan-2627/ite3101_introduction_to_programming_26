from typing import List

n = ["Michael", "Lieberman"]
# Add your function here

def Join_string(words: List[str]) ->str:
    result=""
    for word in words:
        result += word
    return result

print(join_strings(n))
