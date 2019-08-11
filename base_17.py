import string
base=17

def init(base):
    l=[str(x) for x in range(min(base,10))]
    l=''.join(l)
    if base>10:
        l+=string.ascii_lowercase[0:base-10]
    return l

def encode(n,base):
    l=init(base)
    d={}
    count=0
    for i in l:
        d[i]=count;count+=1
    n=n[::-1]
    sum=0
    for i in range(len(n)):
        sum+=int(base**i)*d[n[i]]
    print(sum)
base=2
n='10000'
encode(n,base)