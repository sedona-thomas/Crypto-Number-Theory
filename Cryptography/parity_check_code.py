#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 18:33:20 2020

@author: sedonathomas
"""

import numpy as np

class ParityCheck(object):

    # [n, n-1] code
    def parity_check_code(self, code):
        code = list(str(code))
        main_code, parity_check = code[:-1], int(code[-1])
        check = sum([int(char) for char in main_code]) % 2
        return (check == parity_check)

    def generator_matrix(self, n):
        k = n-1
        I_k, p = np.identity(k), self.P_matrix(n)
        G = np.hstack((I_k, P))
        return G

    def P_matrix(self, n):
        return np.ones((n-1, 1))

    def H_matrix(self, P):
        P_T_neg = (-1 * np.transpose(P)) % 2
        I_k = np.identity(len(P_T_neg))
        H = np.hstack((P_T_neg, I_k))
        return H


