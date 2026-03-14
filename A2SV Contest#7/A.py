n = int(input())
cards = list(map(int,input().split()))

left = 0
right = n-1
s = 0
d = 0
turn = 0
pick = 0
while left<= right:
    if cards[left]>cards[right]:
        pick=cards[left]
        left+=1
    else:
        pick=cards[right]
        right -=1
    
    if turn%2 == 0:
        s+=pick
    else:
        d+=pick
    turn+=1

print(s , d)