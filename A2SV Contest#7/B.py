t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    sum_crowd = a[0] + a[1]
    sum_elite = a[-1]
    crowd = 2
    elite = 1
    l = 2
    r = n - 2
    ok = False
    while l <= r:
        if sum_elite > sum_crowd and elite < crowd:
            ok = True
            break
        sum_crowd += a[l]
        crowd += 1
        l += 1
        
        sum_elite += a[r]
        elite += 1
        r -= 1
    
    if sum_elite > sum_crowd and elite < crowd:
        ok = True
    
    if ok:
        print("YES")
    else:
        print("NO")