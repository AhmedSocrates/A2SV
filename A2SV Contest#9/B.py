t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    target = abs(arr[0])
    count = 0
    for i in range(1,n):
        if abs(arr[i]) >= target:
            count+=1
    check = (n-1) // 2 
    if count >= check:
        print("YES")
    else:
        print("NO")
