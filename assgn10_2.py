name=input('Enter file name: ')
handle=open(name)

di=dict()
for line in handle:
    if line.startswith("From:"):
        continue
    elif line.startswith('From'):
        words=line.split()
        time=words[5]
        hrl=time.split(':')
        for hr in hrl[:1]:
                di[hr]=di.get(hr,0)+1

dis=sorted([(k,v) for k,v in di.items()])
for key,value in dis[:]:
    print(key, value)
