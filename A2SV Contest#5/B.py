days = int(input())
count = {}
for day in range(days):
    m = int(input())
    day_seen = set()
    for _ in range(m):
        s,h = input().split()
        h = int(h)
        day_seen.add((s,h))

    for val in day_seen:
        count[val] = count.get(val, 0) + 1  
    
rcp = (80*days + 99) // 100 

for v in count.values():
    if v >= rcp:
        print("YES")
        break
else:
    print("NO")