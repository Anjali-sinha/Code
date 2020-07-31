name=input('Enter file name: ')
handle=open(name)

dicts=dict()
for line in handle:
    if line.startswith("From:"):
        continue
    elif line.startswith('From'):
        word=line.split()
        for words in word:
            if word.index(words)==1:
                dicts[words]=dicts.get(words,0)+1

bigcount=None
bigword=None
for key,value in dicts.items():
    if bigcount is None or value>bigcount:
        bigcount=value
        bigword=key

print(bigword, bigcount)
