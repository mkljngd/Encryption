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
    return sum

base=30
# n=['74', '97', '97', '107', '101', '32', '82', '101', '99', '111', '114', '100', '32', '109', '97', '105', '44', '32', '73', '110', '115', '97', '97', '110', '32', '104', '97', '105', '32', '121', '97', '32', '66', '104', '97', '103', '119', '97', '97', '110']
# for i in n:
#     decode(i,base)
decode('08DP',base)
