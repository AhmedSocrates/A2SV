t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = int(input())
    if min(a) <= b <=max(a):
        print("YES")
    else:
        print("NO")