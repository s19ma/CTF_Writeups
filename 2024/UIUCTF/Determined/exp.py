from pwn import*
from Crypto.Util.number import*
from Crypto.Util.number import bytes_to_long, long_to_bytes
from itertools import permutations
from sage.all import*

def fun(M):
    def sign(sigma):
        l = 0
        for i in range(5):
            for j in range(i + 1, 5):
                if sigma[i] > sigma[j]:
                    l += 1
        return (-1)**l

    res = 0
    for sigma in permutations([0,1,2,3,4]):
        curr = 1
        for i in range(5):
            curr *= M[sigma[i]][i]
        res += sign(sigma) * curr
    return res


context.log_level = "debug"

io = process(["python", "server.py"])

a = [[1]*9, [1, 1, 1, 2, 1, 2, 1, 2, 1], [2, 1, 3, 1, 3, 1, 2, 3, 1]]
# print(a)

res = []
for ai in a:
    # io = process(["python", "server.py"])
    io = remote("determined.chal.uiuc.tf", 1337, ssl = True)
    io.recvline()
    for aj in ai:
        io.sendlineafter(b"=", str(aj).encode())
    res.append(int(io.recvlineafter(b"[DET] Have fun: ").decode()))
    io.close()
print(res)
p, q, r = var("p, q, r")
eqs = []
for i in range(3):
    ai = a[i]
    M = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]

    M[0][0] = p
    M[0][2] = ai[0]
    M[0][4] = ai[1]

    M[1][1] = ai[2]
    M[1][3] = ai[3]

    M[2][0] = ai[4]
    M[2][2] = ai[5]
    M[2][4] = ai[6]

    M[3][1] = q
    M[3][3] = r

    M[4][0] = ai[7]
    M[4][2] = ai[8]

    eq = fun(M)
    eqs.append(eq == res[i])

print(eqs)
ans = solve(eqs, p, q, r)
print(ans)