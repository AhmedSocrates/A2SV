t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    largest = max(a)
    ans = []
    for i in range(m):
        o,l,r = input().split()
        l,r = int(l), int(r)

        if l <= largest <= r:
            if o == "+":
                largest +=1
            else:
                largest -=1
        ans.append(str(largest))
    print (" ".join(ans))