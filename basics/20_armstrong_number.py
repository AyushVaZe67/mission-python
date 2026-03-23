n = int(input('Enter number: '))
temp = n
length = len(str(n))
total = 0

while temp > 0:
    digit = temp % 10
    total = total + digit ** length
    temp = temp // 10

if total == n:
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong number")