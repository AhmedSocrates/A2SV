t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    s = s.lower()
    sound = ""
    for char in s:
        if not sound:
            sound += char
        if sound[-1] != char:
            sound += char
    if sound == "meow":
        print("YES")
    else:
        print("NO")
