def is_palindrom(n):
    s = str(n)
    if s == s[::-1]:
        return True
    return False

def product():
    naj = 0
    for i in range(1,1000):
        for j in range(1,1000):
            if is_palindrom(i*j) == True and i*j >= naj:
                naj = i*j
    return naj

print(product())