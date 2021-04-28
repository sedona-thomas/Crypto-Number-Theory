#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Sedona Thomas
"""


class HillCipher(object):

    # key = [[], ...]
    def hill_cipher_encrypt(self, code, key):
        dimensions = [len(key), len(key[0])]
        for row in range(dimensions[0])    :
            for column in range(dimensions[1]):
                key[row][column] = self.ensure_numeric_key(key[row][column])
    
    # key = [[], ...]
    def hill_cipher_decrypt(self, code, key):
        dimensions = [len(key), len(key[0])]
        for row in range(dimensions[0])    :
            for column in range(dimensions[1]):
                key[row][column] = self.ensure_numeric_key(key[row][column])
                
    # contains letter:number and number:letter
    def letter_number_dictionary(self):
        letters = list("abcdefghijklmnopqrstuvwxyz")
        d = {}
        for x in range(len(letters)):
            d[letters[x]] = x+1
        for x in d.keys():
            d[d[x]] = x
        return d
    
    def standard_letter_to_number(self, string):
        d = self.letter_number_dictionary()
        return d[string]
    
    def standard_letter_to_number_list(self, string):
        d = self.letter_number_dictionary()
        string = list(string.lower())
        li = []
        for x in string:
            li.append(d[x])
        return li
                
    def ensure_numeric_key(self, key):
        if type(key) == str:
            key = list(key.lower())
        if type(key[0]) == str:
            for x in range(len(key)):
                if type(key[x]) == str:
                    key[x] = self.standard_letter_to_number()
        return key
    
    def matrix_multiplication(m1, m2):
        answer = []
        for i in range(len(m1)):
            li = []
            for k in range(len(m2[0])):
                li.append(0)
            answer.append(0)
        for i in range(len(m1)):
           for j in range(len(m2[0])):
               for k in range(len(m2)):
                   answer[i][j] += m1[i][k] * m2[k][j]
        return answer
