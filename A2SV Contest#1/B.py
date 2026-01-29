k,n,w = map(int,input().split())

arr = []
for i in range(w):
    value = k*(i+1)
    arr.append(value)

total = sum(arr)
if total <=n:
    print(0)
else:
    print(total -n)    