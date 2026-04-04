n = int(input())
arr = list(map(int,input().split()))
curr = 0
rest = 0

for i in range(2*n):
    if arr[i%n] == 1:
        curr += 1
        if curr >= rest:
            rest = curr
    else:
        curr = 0

print(rest)

