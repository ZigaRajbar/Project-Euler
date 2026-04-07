def razcep(n):
    largest = -1
    
    # Remove factor 2
    while n % 2 == 0:
        largest = 2
        n //= 2
    
    # Check odd factors from 3 onwards
    i = 3
    while i * i <= n:
        while n % i == 0:
            largest = i
            n //= i
        i += 2
    
    # If n > 1, then it's a prime factor
    if n > 1:
        largest = n
    
    return largest

print(razcep(600851475143))

600851475143