from collections import Counter
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    a.sort(reverse=True)
    mx = 0
    turn = 0
    while True:
        move_found = False
        for i in range(len(a)):
            if a[i] >=mx:
                mx = a[i]
                move_found = True
                turn ^=1
                break
        if not move_found:
            break
    
    if turn == 1:
        print("YES")
    else:
        print("NO")