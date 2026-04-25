t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    ans = 0
    flag = False

    for i in range(n-1):
        if arr[i]>0:
            ans+=arr[i]
        if arr[i] == 0:
            ans+=1
        
    print(ans)   
