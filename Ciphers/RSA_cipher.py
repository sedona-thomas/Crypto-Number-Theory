#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Sedona Thomas
"""

class RSAMethods(object):

    '''
        input:  p, q = primes
                e = number such that gcd(e, phi(n)) = 1
        output: modular inverses d and e of phi(n)
    '''
    
    def RSA(self, p, q, e):
        n = p * q
        phi_n = self.phi(n)
        if self.RSA_gcd(e, phi_n) != 1:
            print("Error: gcd(e, phi(n)) != 1")
            return -1
        d = self.RSA_mod_inverse(e, phi_n)
        return e, d
    
    '''
        input:  m = message
                n = product of primes
                e = number such that gcd(e, phi(n)) = 1
        output: encryped message
    '''
    def RSA_encrypt(self, m, n, e):
        x = self.prime_factors(n)
        p, q = x[0][0], x[1][0]
        e, d = self.RSA(p, q, e)
        return (m**e) % (p*q)
    
    '''
        input:  m = message
                n = product of primes
                e = number such that gcd(e, phi(n)) = 1
        output: decryped message
    '''
    def RSA_decrypt(self, m, n, e):
        x = self.prime_factors(n)
        p, q = x[0][0], x[1][0]
        e, d = self.RSA(p, q, e)
        return (m**d) % (p*q)
    
    '''
        input:  m = message
                p, q = primes
                e = number such that gcd(e, phi(n)) = 1
        output: encryped message
    '''
    def RSA_encrypt_p_q(self, m, p, q, e):
        e, d = self.RSA(p, q, e)
        return (m**e) % (p*q)
    
    '''
        input:  m = message
                p, q = primes
                e = number such that gcd(e, phi(n)) = 1
        output: decryped message
    '''
    def RSA_decrypt_p_q(self, m, p, q, e):
        e, d = self.RSA(p, q, e)
        return (m**d) % (p*q)    


    '''
    input:  a, b = integers
    output: int(GCD) of a and b
    '''  
    def RSA_gcd(self, a, b):  
        return a if b == 0 else self.RSA_gcd(b, (a % b)) 
        
       
    '''
        input:  k = integer
                mod = modulus
        output: k^-1 = the modular inverse of k
                k * k^-1 = 1 % mod
    '''
    def RSA_mod_inverse(self, k, mod):
        x = k % mod
        for i in range(1, mod):
            if ((x * i) % mod == 1):
                return i
        print("Error: no inverse for {} (mod {})".format(k, mod))
        return -1

    '''
        input:  n = some number for \phi(n)
        output: \phi(n)
    '''
    def phi(self, n):
        n, li, phi = self.prime_factors(n), [], 1
        for x in n:
            prime, power = x[0], len(x)
            li.append(self.eulers_phi_function(prime, power))
        for x in li:
            phi *= x
        return phi
    
    def eulers_phi_function(self, n, p):
        return n**p - n**(p-1)
        
    def prime_factors(self, n):
        factors, i = [], 2
        while n > 1:
            li = []
            while n % i == 0 and n > 1:
                n = n / i
                li.append(i)
            if len(li) > 0:
                factors.append(li)
            i += 1
        return factors
        
   

