t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    ok = True
    for i in range(1, n):
        if arr[i] - arr[i-1] > 1:
            ok = False
            break
    if ok:
        print("YES")
    else:
        print("NO")