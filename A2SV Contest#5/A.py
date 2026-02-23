w1,t1 = map(int,input().split())

n = int(input())
flag = False
for i in range(n):
    w2,t2 = map(int,input().split())
    if w1 < w2 or (w1 == w2 and t1 > t2):
        flag = True 
if flag:
    print("The Fallen Champion")
else:
    print("The Champion Saves the Accused")