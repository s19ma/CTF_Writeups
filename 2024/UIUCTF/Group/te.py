from sympy.ntheory import sieve, isprime, prime
from sympy.core import integer_nthroot
from math import lcm, gcd, isqrt
from tqdm import*   
from Crypto.Util.number import*

k = 10**170 + 8786356
n = (6*k+1)*(12*k+1)*(18*k+1)

print(n)