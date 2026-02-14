t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))

    int_arr = [0]*n
    result = 0
    m = max(arr)
    unique_p = set()
    has_zero = False
    for i in range(n):
        if arr[i] == 0:
            has_zero = True
        else:
            unique_p.add(arr[i])

    k = len(unique_p)
    if k == 0:
        result = 0
    elif has_zero:
        result = 2*k
    else:
        result = 2*k-1
    print(result) 