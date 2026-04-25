t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    b_index = 0
    for i in range(n):
        if s[i] <= s[b_index]:
            b_index = i
    ans = s[b_index] + s[:b_index] + s[b_index+1:]
    print(ans)