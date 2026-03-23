n = int(input())
temp = n

prod1 = 1
sum1 = 0
while temp > 0:
    rem = temp % 10
    sum1 += rem
    prod1 *= rem
    temp = temp // 10

print(abs(prod1-sum1))
