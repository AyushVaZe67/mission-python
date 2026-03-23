candies = [1,2,3,4,6]
maxCandies = max(candies)
extraCandies = int(input())

ans = []

for i in candies:
    if (i + extraCandies) > maxCandies:
        ans.append(True)
    else:
        ans.append(False)

print(ans)
print([True if (i + extraCandies) > maxCandies else False for i in candies])