n=input()
n1=int(n)
if n1%2!=0:
    print("Weird")
else:
    if 2<n1<5:
        print("Not Weird")
    elif 6<n1<20:
        print("Weird")
    else:
        print("Not Weird")            
