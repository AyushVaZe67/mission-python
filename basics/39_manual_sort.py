l1 = [2,4,6,5,3,8,7,9,1]

for i in l1:
    for j in range(len(l1)-1):
        if l1[j] > l1[j+1]:
            l1[j], l1[j+1] = l1[j+1], l1[j]

print(l1)