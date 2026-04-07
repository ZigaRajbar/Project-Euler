def vsota_kvadratov(n):
    if n < 1:
        return n
    return n**2 + vsota_kvadratov(n-1)

def kvadrat_vsote(n):
    vsota = 0
    for stevilka in range(1, n+1):
        vsota += stevilka
    return vsota**2

def razlika(n):
    return kvadrat_vsote(n) - vsota_kvadratov(n)

print(razlika(100))