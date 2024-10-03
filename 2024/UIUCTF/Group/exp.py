from pwn import*
from Crypto.Util.number import*
from random import randint
from math import gcd, log
import time
from Crypto.Util.number import *
from sage.all import*
from sympy.ntheory.residue_ntheory import _discrete_log_pohlig_hellman


c = 34753038154411211682095872795349553162426516208639680024090537129661552898270957264799714036402944845104068313712723435418451767043376579275451063586505192001
# c = 11288547949888365506879695832689507289066486160751190483608287038499660488008998490836209319750056926495280709887700590202486599527192386140988018329491770865105576250858297617404760569424681
context.log_level = "debug"
io = remote("groups.chal.uiuc.tf", 1337, ssl = True)
# io.recvline()
io.sendlineafter(b"c = ", str(c).encode())
a = int(io.recvlineafter(b"a = ").decode())
b = int(io.recvlineafter(b"b = ").decode())
# io.recvline()
io.interactive()
#uiuctf{c4rm1ch43l_7adb8e2f019bb4e0e8cd54e92bb6e3893}