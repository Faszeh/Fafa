def josephus(n, k):
    if n == 1:
        return 1
    else:
        return (josephus(n - 1, k) + k - 1) % n + 1

x = int(input())
for _ in range(x):
    n, k = 100, 2
    while True:
        line = input().strip()
        if line == "*":
            break
        parts = line.split()
        if parts[0] == 'n':
            n = int(parts[1])
        elif parts[0] == 'k':
            k = int(parts[1])
    print(josephus(n, k))
