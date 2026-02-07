t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    sumOfHealth = []
    reached = False
    for i in range(n):
        sumOfHealth += matrix[0][i]
    list = []
    for b in range(n):
        list.append(abs(matrix[1][n]))
    list.sort()
    #Noooo tiiiime 
    for c in range(len(list)):
        list[0]-=1
        
        sumOfHealth-=k
        if(list[c] == 0):
            reached = True
        e