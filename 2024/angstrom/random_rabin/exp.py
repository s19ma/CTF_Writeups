from pwn import*
from Crypto.Util.number import*

from sage.all import*
from Crypto.Util.number import*
import sys
sys.path.append("../../../../Tools/coppersmith")
from coppersmith_multivariate_heuristic import coppersmith_multivariate_heuristic

def solve_if_not_res(n, m):

    m = int(m)
    n = int(n)
    c = (pow(m, 2, n))
    x, k = PolynomialRing(Zmod(n), "x, k").gens()
    f = x**2 - c + k*n
    bnd = 2**128-1
    ans = coppersmith_multivariate_heuristic(f, [bnd, bnd], 1.0)[0]
    res = ans[0]
    if res == 2**128 or res == 2**128-1:
        return solve_if_not_res(n, m)
    return res

# context.log_level = "debug"
io = remote("challs.actf.co", 31300)
# io = process(["python", "random_rabin.py"])
for i in range(64):
    print(f"{i = }")
    io.recvuntil(b"pubkey: ")
    n = int(io.recvline().decode())
    io.recvuntil(b"plaintext: ")
    plt = int(io.recvline().decode())
    if (plt.bit_length()==128 or ((-plt)%n).bit_length()==128):
        ress = plt if plt.bit_length()==128 else (-plt)%n
    else:
        ress = solve_if_not_res(n, plt)
    ress = long_to_bytes(ress).hex()
    io.sendlineafter(b"gimme the secret:" ,ress.encode())

#actf{f4ncy_squ4re_r00ts_53a370c33f192973}
io.interactive()