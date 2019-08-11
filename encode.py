#from decimal to base to base...
import string

#from decode import init2

d1={}  #count to char
d2={}  #char to count

def init1(base):
    l=[str(x) for x in range(min(base,10))]
    l=''.join(l)
    if base>10:
        l+=string.ascii_uppercase[0:base-10]
    count=0
    for i in l:
        d1[str(count)]=i
        d2[i]=count
        count+=1


def dec_value(x,base):
    if x.isdigit():
        return int(x)
    else:
        sum=0
        x=x[::-1]
        for i in range(len(x)):
            sum+=int(base**i)*int(d2[n[i]])
        print(x,sum)
        return sum;
def encode(n,base):
    l=[]
    x=dec_value(n,base)
    init1(base)
    while(int(x)>0):
        l.append(str(int(x)%base))
        x=int(int(x)//base)
    l=l[len(l)::-1]
    l1=[d1[y] if int(y)>9 else y for y in l]
    l1=''.join(l1)
    return l1

n='665123'
base=30
x=encode(n,base)
print(x)
y=encode(x,base)
print(y)