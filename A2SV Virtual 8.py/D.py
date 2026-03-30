from collections import Counter

t = int(input())

for _ in range(t):
    n,c,d = map(int, input().split())
    a = list(map(int, input().split()))

    freq = Counter(a)
    a11 = min(a)
    
    ok = True 
    for i in range(n):
        for j in range(n):
            val = a11 + i * c + j * d
            if freq[val] == 0:
                ok = False
                break
            freq[val] -= 1
        if not ok:
            break 
    print("YES" if ok else "NO")