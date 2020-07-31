# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
count=0
sum=0
fh = open(fname)
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count=count+1
        inp=float(line[20:])
        sum=sum+inp
print('Average spam confidence:', sum/count)
