t = int(input())
#number of opertations needed to form a equillibrium tringle 
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    ans = float('inf')    
    for i in range(n-2):
        cost = arr[i+2] - arr[i]
        ans = min(ans,cost)
    print(ans)
