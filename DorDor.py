def analyze_flights():
    n, m = map(int, input().split())
    cities = []
    for _ in range(n):
        cities.append(input().strip())
    
    flight_map = {city: [] for city in cities}
    
    for _ in range(m):
        start, end = input().split()
        flight_map[start].append(end)
    
    for city in cities:
        if flight_map[city]:
            print(len(flight_map[city]), *flight_map[city])
        else:
            print(0)



analyze_flights()
