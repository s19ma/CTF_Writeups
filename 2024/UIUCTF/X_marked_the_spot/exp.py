from pwn import*
from Crypto.Util.number import*
from itertools import cycle

with open("ct", "rb") as ct_file:
    ct = ct_file.read()


flag = b"uiuctf{????????????????????????????????????????}"

key = []
key[:7] = xor(flag[:7], ct[:7])


key.append(ord(xor(flag[-1], ct[-1])))
# print(bytes(key))
key = bytes(key)

flag = bytes(x ^ y for x, y in zip(ct, cycle(key)))

print(flag)
#uiuctf{n0t_ju5t_th3_st4rt_but_4l50_th3_3nd!!!!!}