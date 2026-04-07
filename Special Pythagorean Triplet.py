def je_trojcek (a, b, c):
    if a < b < c and a**2 + b**2 == c**2:
        return True
    return False

def poseben():
    for a in range(1, 1000):
        for b in range(a + 1, 1000):
            c = 1000 - a - b
            if je_trojcek(a, b, c):
                return a*b*c

print(poseben())