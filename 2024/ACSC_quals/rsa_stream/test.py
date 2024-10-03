import random
from Crypto.Util.number import getPrime
from output import n
from tqdm import*

text = open("chal_redacted.py", "rb").read()
ctext = open("chal.py.enc", "rb").read()
check=""
for b, c in zip(text, ctext):
    o = 0
    for i in range(8):
        bit = ((b >> i) & 1) ^ ((c>>i)&1)
        check += str(bit)

k=1
lb, ub = 0, n
for i in trange(n.bit_length()):
    if check[k]=="1":
        lb = (ub+lb)//2             
        k+=1
    else:
        ub = (ub+lb)//2
        k+=1
# print(ub, lb)
for bound in trange(-1000, 1000):
    m = ub+bound
    ciphertexts = []
    ctext = open("chal.py.enc", "rb").read()
    for c in ctext:
        o = 0
        for i in range(8):
            bit = ((c >> i) & 1) ^ ((m) % 2)
            m = (2*m)%n
            o |= bit << i
        ciphertexts.append(o)


    if b"ACSC{" in bytes(ciphertexts):
        print(f"real_m =  {ub + bound}")
        # print(f"{bound = }")
        open("chal_solve.py", "wb").write(bytes(ciphertexts))
        break
        
    
    # f = open("chal_solve.py", "rb").read()