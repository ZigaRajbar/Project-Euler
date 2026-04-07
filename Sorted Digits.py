def sortiraj(n):
    n = str(n)
    sortirano = ''
    for i in range(len(n)):
        sortirano += sorted(n)[i]
    return sortirano

def funkcija(d):
    d = str(d)
    novo_stevilo = ''
    for i in range(len(d)):
        if int(d[i]) == 0:
            novo_stevilo += ''
        else:
            novo_stevilo += d[i]
    return sortiraj(novo_stevilo)

def vsota(n):
    vs = 0
    d = 1
    while d < n:
        vs += int(funkcija(d)) 
        d += 1
    return vs

print(vsota(100000))
