t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    result = 0
    total_candy = sum(arr)
    if(total_candy%n != 0):
        result = -1
    else:
        target = total_candy // n
        k = 0
        for candy in arr:
            if candy>target:
                k+=1
        result = k
    print(result)
