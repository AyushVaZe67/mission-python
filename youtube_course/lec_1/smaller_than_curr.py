nums = [9,2,4,4,1] #[4,1,2,2,0]
final = []

for i in nums:
    count = 0
    for j in nums:
        if j < i:
            count += 1

    final.append(count)



print(final)