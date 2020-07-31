if __name__ == '__main__':
    arr=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append(score)
low=min(arr)
arr.remove(low)
for ar in arr:
    if ar ==low:
        arr.remove(ar)
        
