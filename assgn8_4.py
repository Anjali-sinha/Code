fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    st=line.split()
    for word in st:
        if word  not in lst:
            lst.append(word)
            lst.sort()
print(lst)
