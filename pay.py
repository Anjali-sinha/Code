hrs = input("Enter Hours:")
rate=input("Enter rate:")
h = float(hrs)
ra=float(rate)
if h>40:
    x1=40*ra
    x2=(h-40)*(ra*1.5)
    pay=x1+x2
else:
    pay=h*ra
print(pay)
