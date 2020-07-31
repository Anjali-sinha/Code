smallest=None
largest=None
while True:
    Num = input("Enter a number: ")
    if Num == "done":
        break
    try:
        num=int(Num)
    except:
        print("Invalid input")
        continue
    if largest is None:
        largest=num
    elif num>largest:
        largest=num
    if smallest is None:
        smallest=num
    elif num<smallest:
        smallest=num
print("Maximum is", largest)
print("Minimum is", smallest)
