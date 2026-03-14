t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    earns = [0] * (k+1)
    for i in range(k):
        a,b = map(int,input().split())
        earns[a] += b 
    earns.sort(reverse = True)
    print(sum(earns[:n]))