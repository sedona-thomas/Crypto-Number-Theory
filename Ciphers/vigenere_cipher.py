#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Sedona Thomas
"""


class VigenereCipher(object):

    def __init__(self):
        self.low_abc = "abcdefghijklmnopqrstuvwxyz"
        self.letter_number_dictionary = self.letter_number_dictionary()

    # possible_keys = 26**keylength
    def vigenere_cipher_encrypt(self, code, key):
        key = self.ensure_numeric_key(key)
        keylength, string, i = len(key), "", 0
        for char in code:
            string += self.encrypt_character(char, key[i])
            i = (i + 1) % keylength
        return string
    
    def vigenere_cipher_decrypt(self, code, key):
        key = self.ensure_numeric_key(key)
        keylength, string, i = len(key), "", 0
        for char in code:
            string += self.decrypt_character(char, key[i])
            i = (i + 1) % keylength
        return string
        
    def encrypt_character(self, ch, key):
        if ch.isalpha():
            i = (self.low_abc.find(ch) + key) % 26
            return self.low_abc[i].upper() if ch.isupper() else self.low_abc[i]
        else: return ch
    
    def decrypt_character(self, ch, key):
        if ch.isalpha():
            i = (self.cipher.find(ch) - key) % 26
            return self.low_abc[i].upper() if ch.isupper() else self.low_abc[i]
        else: return ch

    def ensure_numeric_key(self, key):
        if type(key) == str:
            key = list(key.lower())
        if type(key[0]) == str:
            for x in range(len(key)):
                if type(key[x]) == str:
                    key[x] = self.low_abc.find(key[x].lower())
        return key
    
    # contains letter:number and number:letter
    def letter_number_dictionary(self):
        letters, d = list(self.low_abc), {}
        for x in range(len(letters)):
            d[letters[x]] = x+1
        for x in d.keys():
            d[d[x]] = x
        return d
    
    def standard_letter_to_number(self, string):
        return self.letter_number_dictionary[string]
    
    def standard_letter_to_number_list(self, string):
        d = self.letter_number_dictionary
        string, li = list(string.lower()), []
        for x in string:
            li.append(d[x])
        return li