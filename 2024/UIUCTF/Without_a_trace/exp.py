from pwn import*
from Crypto.Util.number import*
from sage.all import*
import numpy as np
from Crypto.Util.number import bytes_to_long
from itertools import permutations
from Crypto.Util.Padding import pad
context.log_level = "debug"

a = [[1, 2, 3, 4, 5], [2, 1, 4, 3, 5], [3, 1, 2, 3, 6], [1, 4, 3, 5, 2], [4, 5, 3, 1, 2]]
# a = 1
# io.sendlineafter(b"[WAT] u1 = ", )
res = []
for ai in a:
    # io = process(["python", "server.py"])
    io = remote("without-a-trace.chal.uiuc.tf", 1337, ssl = True)
    io.recvline()
    for aj in ai:
        io.sendlineafter(b"=", str(aj).encode())
    res.append(int(io.recvlineafter(b"[WAT] Have fun: ").decode()))
    io.close()
print(res)

a = matrix(a)
res = vector(res)

flag = a.solve_right(res)
flag = b"".join([long_to_bytes(int(i)) for i in flag]).decode()
print(flag)
#uiuctf{tr4c1ng_&&_mult5!}  