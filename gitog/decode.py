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
    return str(sum)

base=30
n=['2E', '37', '37', '3H', '3B', '12', '2M', '3B', '39', '3L', '3O', '3A', '12', '3J', '37', '3F', '1E', '12', '2D', '3K', '3P', '37', '37', '3K', '12', '3E', '37', '3F', '12', '41', '37', '12', '26', '3E', '37', '3D', '3T', '37', '37', '3K']
l=[decode(x,base) for x in n]
print(l)
