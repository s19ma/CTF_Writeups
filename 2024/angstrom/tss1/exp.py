from pwn import*
from Crypto.Util.number import*
context.log_level = "debug"
from hashlib import sha256
import fastecdsa.curve
import fastecdsa.keys
import fastecdsa.point
curve = fastecdsa.curve.secp256k1

def hash_transcript(pk, R, msg):
	h = sha256()
	h.update(f'({pk.x},{pk.y})'.encode())
	h.update(f'({R.x},{R.y})'.encode())
	h.update(msg)
	return int.from_bytes(h.digest(), 'big') % curve.q

def recvlineafter(msg):
    io.recvuntil(msg)
    to_recv = io.recvline()
    return to_recv

def verify(pk, msg, sig):
	c, s = sig
	R = s * curve.G + c * pk
	return c == hash_transcript(pk, R, msg)

io = remote("challs.actf.co", 31301)

sk1, pk1 = fastecdsa.keys.gen_keypair(curve)
# k1, R1 = fastecdsa.keys.gen_keypair(curve)

pub_key = eval(recvlineafter(b"my public key: "))
pub_keyx = pub_key[0]
pub_keyy = pub_key[1]
pub_key = fastecdsa.point.Point(pub_keyx, pub_keyy, curve=curve)

pub_key_send = -pub_key+curve.G
io.sendlineafter(b"x", str(pub_key_send.x).encode())
io.sendlineafter(b"y", str(pub_key_send.y).encode())
apk = eval(recvlineafter(b'aggregate public key: '))

print(f"{apk = }")
apkx = apk[0]
apky = apk[1]
apk = fastecdsa.point.Point(apkx, apky, curve=curve)
io.sendlineafter(b'message: ', b"3".hex())

R1 = eval(recvlineafter("my nonce: ").decode())
R1x = R1[0]
R1y = R1[1]
R1 = fastecdsa.point.Point(R1x, R1y, curve=curve)
R2 = -R1+curve.G

io.sendlineafter(b"x", str(R2.x).encode())
io.sendlineafter(b"y", str(R2.y).encode())

R = eval(recvlineafter("aggregate nonce: "))
Rx = R[0]
Ry = R[1]
R = fastecdsa.point.Point(Rx, Ry, curve=curve)
print(R)

s= int(recvlineafter(b"my share of the signature: ").decode())
msg = b"flag"
c = hash_transcript(apk, R, msg)
s = (-c+1) % curve.q
print(s*curve.G + c*apk == R)
io.sendlineafter(b"c: ", str(c).encode())
io.sendlineafter(b"s: ", str(s).encode())
io.recvline()
#actf{r0gu3_4ggr3g4t1on_632d50edb72d34d3}