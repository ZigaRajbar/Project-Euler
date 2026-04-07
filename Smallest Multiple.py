delitelji = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]

def je_deljivo(n):
    for element in delitelji:
        if n % element != 0:
            return False
    return True

def najmanjsi():
    i = 1
    while True:
        if je_deljivo(i) == True:
            break
        i +=1
    return i

print(najmanjsi())