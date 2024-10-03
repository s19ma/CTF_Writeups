from pwn import*
from Crypto.Util.number import*
from Crypto.Util.number import isPrime, getPrime, long_to_bytes, bytes_to_long
from Crypto.Random.random import getrandbits, randint
from Crypto.Hash import SHA512
import random
import secrets 

def hash(val, bits=1024):
    output = 0
    for i in range((bits//512) + 1):
        h = SHA512.new()
        h.update(long_to_bytes(val) + long_to_bytes(i))
        output = int(h.hexdigest(), 16) << (512 * i) ^ output
    return output

context.log_level = "debug"
# io = process(["python", "chal.py"])
io = remote("snore-signatures.chal.uiuc.tf", 1337, ssl = True)

p = int(io.recvlineafter(b"p = ").decode())
q = int(io.recvlineafter(b"q = ").decode())
g = int(io.recvlineafter(b"g = ").decode())

for _ in range(10):
    y = int(io.recvlineafter(b"y = ").decode())

    m = getrandbits(512)
    io.sendlineafter(b"m = ", str(m).encode())
    s = int(io.recvlineafter(b"s = ").decode())
    e = int(io.recvlineafter(b"e = ").decode())

    r = (pow(g, s, p)*pow(y, e, p)) %p

    ss = secrets.randbelow(q)

    rv = (pow(g, ss, p) * pow(y, e, p)) % p
    mm = (r + m - rv)%p
    print(f"{m = }")
    print(f"{mm = }")
    io.sendlineafter(b"m = ", str(mm).encode())
    io.sendlineafter(b"s = ", str(ss).encode())
io.interactive()
#uiuctf{add1ti0n_i5_n0t_c0nc4t3n4ti0n}