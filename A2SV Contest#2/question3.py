password = input()
t = int(input())

arr = [input() for _ in range(t)]
ends = False
starts = False
answer = False
for word in arr:
    if word == password :
        answer = True
    if word[1] == password[0]:
        ends = True
    if word[0] == password[1]:
        starts = True
if (answer or (starts and ends)):
    print("YES")
else: 
    print("NO")

        
 