s1 = input('s: ')
s = s1.lower()
vowels = 0
for c in s:
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
        vowels += 1

print('Vowels: ', vowels)
print('Consonants: ', len(s) - vowels)