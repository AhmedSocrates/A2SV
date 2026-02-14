t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))

    can = True
    for i in range(n):
        if arr[i] <= 2*(max(i,n-1-i)):
            can= False
            break
    if can:
        print("YES")
    else:
        print("NO")
