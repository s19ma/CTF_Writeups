from ptrlib import*
import os
import signal
import base64
import ed25519
io = Socket("nc localhost 3229")
io.debug=True

PHRASE = b'I want flag'
my_sk, my_pk = ed25519.create_keypair()

sig = my_sk.sign(PHRASE)
sig = base64.b64encode(sig)
io.sendlineafter(b">", "1")
key = io.recvlineafter("Your key is: ")

key = base64.b64decode(key)

#print(key)
forge_key = key[:60] + my_sk.sk_s[32:]
forge_key = base64.b64encode(forge_key)

io.sendlineafter(b">", "3")
io.sendlineafter("Hand me your key: ", forge_key)
io.sendlineafter(b"Which message to verify?: ", PHRASE)
io.sendlineafter(b"What is the signature?: ", sig)
io.interactive()