n = int(input())
arr = list(map(int, input().split()))


odd = False
even = False

for x in arr:
    if x % 2 == 0:
        even = True
    else:
        odd = True

if odd and even:
    arr.sort()

print(*arr)