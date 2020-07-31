n = int(input())
arr = list(map(int, input().split()))
zes = max(arr)
arr.remove(zes)
for ar in arr:
    if ar ==zes:
        arr.remove(ar)
print(max(arr))
