l1 = [2,3,4]
l2 = [2,5,6,3]

final = []

for num1 in l1:
    for num2 in l2:
        if num1 == num2:
            final.append(num1)

print(list(set(l1) & set(l2)))

print(final)