def prastevila_pod(n):
    prastevila = [2]
    i = 3
    while prastevila[-1] < n:
        is_prime = True
        for prastevilo in prastevila:
            if i % prastevilo == 0:
                is_prime = False
                break
        if i > n:
            break
        if is_prime:
            prastevila.append(i)
        i += 2
    return prastevila

def vsota_prastevil(n):
    vsota = 0
    for prastevilo in prastevila_pod(n):
        vsota += prastevilo
    return vsota

print(vsota_prastevil(2000000))