s = input()
t = input()

n = len(s)
m = len(t)
vowel1 = False
vowel2 = False
if n != m:
    print("NO")
else:
    for i in range(n):
        if s[i] in 'aeiou':
            vowel1 = True
        if t[i] in 'aeiou':
            vowel2 = True
        if vowel1 != vowel2:
            print("No")
            break
    else:
        print("YES")
        
        
