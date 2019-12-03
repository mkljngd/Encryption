from encode import encode
from decode import decode

x = 20
bases = [2, 4, 6, 9,16]
s_encoded = []

for base in bases:
    print('number = {},base= {},encrypted = {}'.format(x, base, encode(x, base)))
    s_encoded.append(encode(x, base))
    x = encode(x, base)
print(s_encoded)
s_encoded = s_encoded[::-1]
bases = bases[::-1]
num=''
s_decoded = []

for i in range(len(s_encoded)):
    encrypt = s_encoded[i]
    base = bases[i]
    print('encrypted = {}, base = {}, number = {}'.format(
        encrypt, base, decode(encrypt, base)))
    s_decoded.append(decode(encrypt,base))

print(s_decoded)