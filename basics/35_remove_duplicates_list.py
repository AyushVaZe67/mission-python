l1 = [20, 30, 20, 10, 22, 40, 12, 20, 12, 14]

seen = {}
duplicates = []

for num in l1:
    if num in seen:  # First check if key exists
        if seen[num] == 1:  # Then check the value
            duplicates.append(num)
            seen[num] = 2
    else:
        seen[num] = 1

print(duplicates)  # [20, 12]