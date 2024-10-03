from pwn import *
# context.log_level = "debug"
# host = 'reversecryptographing.nc.jctf.pro'
# port = 1337
# conn = remote(host, port)

conn = process(["python", "task.py"])
flag = ''

conn.sendline(b'000000')
correct = conn.recvline().decode()

while True:
    mul = 1
    while True:
        for i in range(256):
            payload = (flag[::-1].encode() + bytes([i]) * 2 * mul + flag.encode() + b'\x00' * 3).hex()
            conn.send(payload.encode() + b'\n')
            response = conn.recvline().decode()

            if response == correct:
                flag = f"{chr(i) * mul}{flag}"
                mul = 1
                print(flag)
                break
        else:
            mul += 1