t = int(input())

for _ in range(t):
    word = input()
    if(len(word) > 10):
        between = len(word) - 2
        print(word[0] + str(between) + word[-1])
    else:
        print(word)