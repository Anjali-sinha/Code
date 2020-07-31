if __name__ == '__main__':
    n = int(input())
    arr =[]
    for _ in range(n):
        x=int(input())
        arr.append(x)
    a=max(arr)
    arr.remove(a)
    b=max(arr)
    print(b)
