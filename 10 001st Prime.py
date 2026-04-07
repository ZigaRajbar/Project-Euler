def prastevilo(n):
    prastevila = [2]
    i = 3
    while len(prastevila) < n:
        for pras in prastevila:
            if i % pras == 0:
                break
        else:
            prastevila.append(i)
        i += 2
    return prastevila[n-1]

print(prastevilo(10001))