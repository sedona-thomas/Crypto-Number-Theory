#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Sedona Thomas
"""

class ChineseRemainderTheorem(object):

    '''
        input:  li = [[a1, n1], ...]
        output: chinese remainder theorem calculations
    '''
    def chinese_remainder_thm(self, li):
        N = 1
        for i in range(len(li)):
            N *= li[i][1]
        print("N = " + str(N))
        s = "w_{} ≡ {}/{} (({}/{})^-1 (mod {})) ≡ {} (({})^-1 (mod {})) "
        s += "≡ {} × {} ≡ {}"
        for i in range(len(li)):
            a, n = li[i][0], li[i][1]
            f1, f2, x = (N, n, N, n, n), (N//n, N//n, n), mod_inverse(N//n, n)
            f3, f4 = (N//n, x), N//n * x
            print(s.format(i, *f1, *f2, *f3, f4) + "\n")
            li[i].append(f4)
        calc, x = "x ≡ (", 0
        for i in range(len(li)):
            a, w = li[i][0], li[i][2]
            calc += "({} × {})".format(a, w)
            if i < len(li)-1:
                calc += " + "
            x += a * w
        calc += ") (mod {})".format(N) + " ≡ {} (mod {})".format(x, N)
        calc += " ≡ {}".format(x % N)
        print(calc)

    '''
        input:  k = integer
                mod = modulus
        output: k^-1 = the modular inverse of k
                k * k^-1 = 1 % mod
    '''
    def mod_inverse(self, k, mod):
        x = k % mod
        for i in range(1, mod):
            if ((x * i) % mod == 1):
                s = "{}d = 1 + {}x = 1 + ({} × {}) = 1 + {} = {}"
                print(s.format(k, mod, mod, (k*i - 1)//mod, k*i - 1, k*i))
                print("d = {}".format(i))
                return i
        return 1


