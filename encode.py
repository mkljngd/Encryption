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

#4', '97', '97', '107', '101', '32', '82', '101', '99', '111', '114', '100', '32', '109', '97', '105', '44', '32', '73', '110', '115', '97', '97', '110', '32', '104', '97', '105', '32', '121', '97', '32', '66', '104', '97', '103', '119', '97', '97', '110']
base=30
# op=[encode(x,base) for x in n]
# print(op)

if __name__ == "__main__":
    print(encode('655615',base))