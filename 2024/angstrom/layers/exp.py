from pwn import*
import itertools
from Crypto.Util.number import*
def xor(key, data):
    return bytes([k ^ d for k, d in zip(key, data)])

context.log_level = "debug"
# io = process(["python", "challenge.py"])
io = remote("challs.actf.co", 31398)
io.sendlineafter(b"Pick 1, 2, or 3 > ", b"1")
io.sendlineafter(b'Your message > ', b"123"*1000)
ln = bytes.fromhex(io.recvline().decode())

# io = process(["python", "challenge.py"])
io = remote("challs.actf.co", 31398)
io.sendlineafter(b"Pick 1, 2, or 3 > ", b"3")
lnres = bytes.fromhex(io.recvline().decode())
print(f"{ln = }")
print(f"{lnres = }")
print(xor(xor(lnres, ln), b"123"*1000))