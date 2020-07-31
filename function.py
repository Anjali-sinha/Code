def computepay(h,r):
    if h>40:
        x=40*r
        y=(h-40)*(r*1.5)
        p=x+y
    else:
        p=h*r
    return p

h= float(input("Enter Hours:"))
r=float(input("Enter rate:"))
print("Pay", computepay(h,r))
