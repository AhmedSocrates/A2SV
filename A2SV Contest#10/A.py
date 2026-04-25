t = int(input())
for _ in range(t):
    n,k = map(int,input().split())

    s = input()

    currentB = s.count('B')
    if currentB ==k:
        print("0")
    elif currentB>k:
        target = currentB-k
        b = 0

        for i in range(n):
            if s[i] == 'B':
                b +=1
            if b == target:
                print("1")
                print