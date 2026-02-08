n = int(input())
for _ in range(n):
    i = int(input())
    k = list(map(int, input().split()))
    result = [0]*i
    for j in range(i):
        k[j]