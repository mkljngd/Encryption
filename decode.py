# from base to decimal 

import string

d={}

def init(base):
    l=[str(x) for x in range(min(base,10))]
    l=''.join(l)
    if base>10:
        l+=string.ascii_uppercase[0:base-10]
    count=0
    for i in l:
        d[i]=count;count+=1
    return d

def decode(n,base):
    d=init(base)
    n=n[::-1]
    sum=0
    for i in range(len(n)):
        sum+=int(base**i)*int(d[n[i]])
    print(sum)

base=30
n='NP26'
decode(n,base)

