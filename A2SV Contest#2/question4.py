n = int(input())
arr = list(map(int, input().split())) 

left = 0 
right = n-1
s = 0
d = 0
turn = 0

while left<= right:
    if(arr[left] > arr[right]):
        pick = arr[left]
        left += 1
    else:
        pick = arr[right]
        right -= 1 

    if turn % 2 == 0:
        s+=pick
    else:
        d+=pick

    turn += 1
print(s,d)

