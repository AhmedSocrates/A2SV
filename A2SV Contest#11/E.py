t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    # An array of length 1 is already non-decreasing
    if n == 1:
        print(0)
        continue
        
    ops = []
    
    ops.append((1, n))
    if (a[0] + a[n-1]) % 2 == 0:
        a[0] = a[n-1]
    else:
        a[n-1] = a[0]
    for i in range(1, n - 1):
        if (a[0] + a[i]) % 2 != 0:
            ops.append((1, i + 1))
        else:
            ops.append((i + 1, n))
            

    print(len(ops))
    for l, r in ops:
        print(l,r)