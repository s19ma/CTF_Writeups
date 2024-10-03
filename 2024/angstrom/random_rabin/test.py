from random import SystemRandom
from Crypto.Util.number import getPrime
from libnum import xgcd

random = SystemRandom()

def primegen():
	while True:
		p = getPrime(512)
		if p % 4 == 3:
			return p

def keygen():
	p = primegen()
	q = primegen()
	n = p * q
	return n, (n, p, q)

def encrypt(pk, m):
	n = pk
	return pow(m, 2, n)

def decrypt(sk, c):
	n, p, q = sk
	yp, yq, _ = xgcd(p, q)
	mp = pow(c, (p + 1)//4, p)
	mq = pow(c, (q + 1)//4, q)
	s = yp * p * mq % n 
	print(f"{s = }")
	t = yq * q * mp % n 
	print(f"{(t - s) %2**128 = }")
	rs = [(s + t) % n, (-s - t) % n, (s - t) % n, (-s + t) % n]
	# print(f"{m = }")
	# for i in rs:
		# print(pow(i, 2, n) == c)
		# print(f"{i = }")
		# print(f"{- i%n = }")
	# return r
	return 3


pk, sk = keygen()
# print(f'pubkey: {pk}')
secret = random.randbytes(16)
m = int.from_bytes(secret, 'big')
print(m)
print(f'plaintext: {decrypt(sk, encrypt(pk, m))}')
# guess = bytes.fromhex(input('gimme the secret: '))

