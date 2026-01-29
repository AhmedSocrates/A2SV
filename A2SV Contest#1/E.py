t = int(input())
for _ in range(t):
    array = list(map(int,input().split()))

    for i in range(5):
        array.sort()
        array[0] +=1
    print(array[0]*array[1]*array[2])