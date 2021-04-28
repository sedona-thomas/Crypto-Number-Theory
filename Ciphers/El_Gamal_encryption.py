#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Sedona Thomas
"""

class ElGamalEncryption(object):

    '''
        input:  p = large prime
                g = primitive root for (mod p)
                a = private power
                t = plaintext to send
                m_r = message received (g^b (mod p))
        output: m_s * g^ab (mod p) = shared secret message
    '''   
    def el_gamal_encryption(self, p, g, a, t, m_r):
        message = self.personal_message(p, g, a)
        secret = self.shared_secret(p, g, a, m_r)
        ciphertext = t * secret
        print("Send the recipient: {}".format(message))
        print("Shared secret: {}".format(secret))
        print("Encrypted message: {}".format(ciphertext))
    
    '''
        input:  p = large prime
                g = primitive root for (mod p)
                a = private power
                t = encrypted message received
                m_r = message received (g^b (mod p))
        output: m_s * g^ab (mod p) = shared message to send
    ''' 
    def el_gamal_decryption(self, p, g, a, t, m_r):
        message = self.personal_message(p, g, a)
        secret = self.shared_secret(p, g, a, m_r)
        plaintext = t / secret
        print("Send the recipient: {}".format(message))
        print("Shared secret: {}".format(secret))
        print("Decrypted message: {}".format(plaintext))
        
    def personal_message(self, p, g, a):
        return (g**a) % p
     
    def shared_secret(self, p, g, a, m):
        return (m**a) % p