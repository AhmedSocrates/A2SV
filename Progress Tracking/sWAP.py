def swap_case(s):
    output = ""
    for a in s:
        if (a.isupper()):
            output+=a.lower()
        elif(a.islower()):
            output+=a.upper()
        else: output+=a
    return output

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)