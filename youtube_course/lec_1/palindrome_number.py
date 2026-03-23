num = 1212121
temp = num
rev = 0

while temp > 0:
    r = temp%10
    temp = temp // 10
    rev = rev * 10 + r

if rev == num:
    print('YES')
else:
    print('NO')