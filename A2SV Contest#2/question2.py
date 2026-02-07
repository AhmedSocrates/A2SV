n = int(input())
word = input()
lower = word.upper()
set_word = set(lower)

if len(set_word) == 26:
    print("YES")
else:
    print("NO")

















    #print("YES" if len(set(input().lower())) >= 26 else "NO")