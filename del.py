import string

d2={}

def init2(base):
    l=[str(x) for x in range(min(base,10))]
    l=''.join(l)
    if base>10:
        l+=string.ascii_uppercase[0:base-10]
    count=0
    for i in l:
        d2[i]=count;count+=1
    print(d2)

init2(30)

x='123ABC'

for i in x:
    if i.isalnum() and not i.isdigit():
        print(i)
        x=x.replace(i,str(d2[i]))
print(x)