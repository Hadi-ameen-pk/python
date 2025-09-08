def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum
result = add(25,12,23,30)
print(result)
