# Write your function below!
def fizz_count(x: list[str]):
    count = 0
    for n in x:
        if n == "fizz":
            count += 1
    return count


print(fizz_count(["fizz", "cat", "fizz"]))
