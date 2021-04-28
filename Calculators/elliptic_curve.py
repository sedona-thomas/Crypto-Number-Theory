#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Sedona Thomas
"""

class EllipticCurve(object):

    def mod_inverse(self, k, mod):
        x = k % mod
        for i in range(1, mod):
            if ((x * i) % mod == 1):
                return i
        print("Error: no inverse for {} (mod {})".format(k, mod))
        return -1
        
    def elliptic_curve_k(self, x, y, p, b, k):
        x1 = x
        y1 = y
        for x in range(k):
            x1, y1 = self.elliptic_curve(x, y, x1, y1, p, b)
        return x1, y1
    
    def elliptic_curve(self, x1, y1, x2, y2, p, b):
        s = ""
        if x1 == x2 and y1 == y2:
            s += "\nm ≡ (3({})^2 + {}) (2{})^(−1) (mod p)".format(x1, b, y1)
            m = (((3 * (x1**2)) + b) * self.mod_inverse((2 * y1), p)) % p
        else:
            s += "\nm ≡ ({} − {}) ({} − {})^(−1) (mod p)".format(y2, y1, x2, x1)
            m = ((y2 - y1) * self.mod_inverse((x2 - x1), p)) % p
        
        s += "\nx = {}^2 - {} - {}".format(m , x1, x2)
        x = m**2 - x1 - x2
        
        s += "\ny = {}({} - {}) - {}".format(m , x1, x, y1)
        y = m*(x1 - x) - y1
        
        s += "\n({}, {}) (mod {}) ≡ ({}, {})".format(x, y, p, x%p, y%p)
        
        x, y = x % p, y % p
        s += "\n({}, {})\n".format(x, y)
        print(s)    
        return x, y

