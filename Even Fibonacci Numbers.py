def vsota(r):
    sum = 0
    for i in range(r):
        if fibo(i) % 2 == 0 and fibo(i) < 4000000:
            sum += fibo(i)
    return sum

def fibo(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

print(vsota(100))