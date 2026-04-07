def odd_square():
    sum = 0
    for i in range(309001):
        if i % 2 != 0:
            sum += i**2
    return sum

print(odd_square())
