l1 = [2,3,4,5,1,2,3]

count = {}

for num in l1:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

print(count)