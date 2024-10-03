from random import randint
from math import gcd, log
import time
from Crypto.Util.number import *
from sage.all import*

p = 29674495668685510550154174642905332730771991799853043350995075531276838753171770199594238596428121188033664754218345562493168782883
p = getPrime(120)
n = p*(313*(p-1) + 1)*(353*(p-1) + 1)
def check(n, iterations=50):
    if isPrime(n):
        return False

    i = 0
    while i < iterations:
        a = randint(2, n - 1)
        if gcd(a, n) == 1:
            i += 1
            if pow(a, n - 1, n) != 1:
                return False
    return True

print(check(n))
print(n.bit_length())
a = randint(1, n-1)
k = randint(2, n-1)
b = pow(a, k, n)
d = discrete_log(IntegerModRing(n)(b), IntegerModRing(n)(a))
print(d)