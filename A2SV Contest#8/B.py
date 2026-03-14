t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    if n == m == 1:
        print(-1)
        continue
    total = n * m
    for i in range(n):
        row = []
        for j in range(m):
            idx = i*m+j
            row.append(matrix[(idx+1) % total])
        print(*row)
