n = int(input('n: '))
total = 0
s = str(n)
for i in range(len(s)):
    total = total + int(s[i])

print(total)