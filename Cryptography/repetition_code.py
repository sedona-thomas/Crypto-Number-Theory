#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 18:09:18 2020

@author: sedonathomas
"""

import numpy as np

class RepetitionCode(object):

    # [n,1] code
    def repetition_code(self, code, k):
        return str(code) * k

    def repetition_correction_prob(self, k, prob_of_error):
        return (1 - (1 - prob_of_error)**k)

    def generator_matrix(self, n):
        k = 1
        I_k, P = np.identity(k), P_matrix(n)
        G = np.hstack((I_k, P))
        return G

    def P_matrix(self, n):
        return np.ones((1, n-1))

    def H_matrix(self, P):
        P_T_neg = (-1 * np.transpose(P)) % 2
        I_k = np.identity(len(P_T_neg))
        H = np.hstack((P_T_neg, I_k))
        return H



