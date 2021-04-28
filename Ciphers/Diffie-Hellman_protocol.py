#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Sedona Thomas
"""

class DiffieHellmanProtocol(object):

    '''
        input:  p = large prime
                g = primitive root for (mod p)
        output: public information p and g
    '''
    def diffie_hellman_protocol(self, p, g):
        return p, g
        
        
    '''
        input:  p = large prime
                g = primitive root for (mod p)
                a = private power
        output: g^a (mod p) = message to send
    '''   
    def d_h_encryption(self, p, g, a):
        return (g**a) % p
    
     
    '''
        input:  p = large prime
                g = primitive root for (mod p)
                a = private power
                m = message received
        output: shared secret message
    '''   
    def d_h_decryption(self, p, g, a, m):
        return (m**a) % p
        
        
    
    
    
    
