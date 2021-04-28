#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Sedona Thomas
"""

class ModularExponentiation(object):

    '''
        input:  b = base
                e = exponent
                m = modulus
        output: each modular equation for exponent in {1,2,...,e}
    '''
    # repeatedly increases the current power
    def modular_exponentiation(self, b, e, m):
        print(self.m_e_helper(1, b, 1, m, e))

    # helper method
    def m_e_helper(self, p, b, e, m, f):
        s = "{}^{} (mod {}) ≡ ({} × {}) (mod {}) ≡ {} (mod {}) ≡ {}"
        f1, f2, f3, f4 = (b, e, m), (p, b, m), (p*b, m), (p * b) % m
        s = s.format(*f1, *f2, *f3, f4)
        return s + "\n" + self.m_e_helper(f4, b, e+1, m, f) if e < f else s

    '''
        input:  b = base
                e = exponent
                m = modulus
        output: each modular equation for 2^exponent in {1,2,...,e}
    '''
    # repeatedly squares the current value
    def modular_exponentiation_square(self, b, e, m):
        print(self.m_e_s_helper(b, b, 1, m, e))

    # helper method
    def m_e_s_helper(self, p, b, e, m, f):
        s = "{}^{} (mod {})≡ {}^(2^{}) (mod {})≡ {}^2 (mod {})≡ {} (mod {})≡ {}"
        f1, f2, f3, f4, f5 = (b,2**e,m), (b,e,m), (p,m), (p**2,m), (p**2) % m
        s = s.format(*f1, *f2, *f3, *f4, f5)
        return s + "\n" + m_e_s_helper(f5, b, e+1, m, f) if e < f else s

