def sieve_and_find():
    n = int(input().strip())
    m = int(input().strip())

    if n < 2:
        print(1 if m == 1 else 0)
        return

    primes = []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    if m <= len(primes):
        print(primes[m - 1])
    else:
        print(0)



sieve_and_find()
