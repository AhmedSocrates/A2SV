t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    reached = False
    died = False
    for c,k in range(n):
        matrix[0][c] -= k
        if (matrix[0][c] == 0):
            c+=1
            matrix[0][c]
        if(matrix[1][k] ==0):
            reached = True
            
        if(matrix[1][k] <=0):
            matrix[1][k]+=1
        else: 
            matrix[1][k]-=1

    #if (reached)
