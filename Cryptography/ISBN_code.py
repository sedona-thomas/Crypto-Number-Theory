#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 17:14:13 2020

@author: sedonathomas
"""

class ISBN(object):

    '''
        Input: ISBN code = a1 - a2 a3 - a4 a5 a6 a7 a8 a9 - a10
        Output: validity of ISBN code
    '''
    def isbn(self, code):
        code, sum = str(code), 0
        if "-" in code:
            english, publisher, book_iden, error_cor_num = code.split("-")
        else:
            english = code[0]
            publisher = code[1:3]
            book_iden = code[3:9]
            error_cor_num = code[9]
        code = "{}{}{}{}".format(english, publisher, book_iden, error_cor_num)
        for j in range(1, 11):
            sum += j * int(code[j-1])
        return ((sum % 11) == 0)
