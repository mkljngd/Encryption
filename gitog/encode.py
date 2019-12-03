#from decimal to base

import string

d={}

def init(base):
    l=[str(x) for x in range(min(base,10))]
    l=''.join(l)
    if base>10:
        l+=string.ascii_uppercase[0:base-10]
    count=0
    for i in l:
        d[str(count)]=i;count+=1
    return d


def encode(n,base):
    l=[]
    x=n
    init(base)
    while(int(x)>0):
        l.append(str(int(x)%base))
        x=int(int(x)//base)
    l=l[len(l)::-1]
    l1=[d[y] if int(y)>9 else y for y in l]
    l1=''.join(l1)
    return l1

l=[74,97,97,107,101,32,100,101,107,104,32,82,101,99,111,114,100,32,109,97,105,44,32,73,110,115,97,97,110,32,104,97,105,32,121,97,32,66,104,97,103,119,97,97,110]
base=30
for i in l:
    print(encode(i,base),end=',')

    '2E,37,37,3H,3B,12,2M,3B,39,3L,3O,3A,12,3J,37,3F,1E,12,2D,3K,3P,37,37,3K,12,3E,37,3F,12,41,37,12,26,3E,37,3D,3T,37,37,3K'