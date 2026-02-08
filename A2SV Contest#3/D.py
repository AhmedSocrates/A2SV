n = int(input())
s = input()
word = "ACTG"

ans = 10000000
for i in range(n-3):
    curr = 0
    for j in range(4):
        cs = ord(s[i+j]) - ord('A')
        ct = ord(word[j]) - ord('A')

        diff = abs(cs-ct)
        opr = min(diff,26-diff)
        curr += opr 

    ans = min(ans,curr)
print(ans)

