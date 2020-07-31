def mutate_string(string, position, character):
    i, c=int(input()), input()
    str=s[:i]+c+s[i+1:]
    return str

if __name__ == '__main__':
    s = input()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
