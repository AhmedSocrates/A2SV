t = int(input())

for i in range(t):
    n,m,p,q = map(int, input().split())
    period = n//p
    remain = n%p

    if remain==0:
        if m==period*q:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")
