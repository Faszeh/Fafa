grade_values = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1, 'F': 0}

n = int(input("تعداد امتحانات: "))

weighted_sum = 0
total_weights = 0

for _ in range(n):
    entry = input().strip()
    weight = int(entry[0])  
    grade = entry[1]        
    weighted_sum += weight * grade_values[grade]  
    total_weights += weight 

weighted_avg = weighted_sum / total_weights

for grade, value in grade_values.items():
    if weighted_avg >= value:
        print(grade)
        break
