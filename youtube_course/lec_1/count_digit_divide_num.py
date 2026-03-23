num = int(input('Num: '))
count = 0
original = num
while num > 0:
    r = num % 10
    if original % r == 0:
        count += 1
    num = num // 10

print(count)
