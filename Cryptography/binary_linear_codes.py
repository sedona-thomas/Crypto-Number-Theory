#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Sedona Thomas
"""

import numpy as np

class BinaryLinearCodes(object):

    def binary_linear_code(self, n, k):
        return n, k

    def minimum_Hamming_distance(self, codes):
        d = len(codes[0])
        for code in codes:
            weight = sum([int(char) for char in code])
            d = weight if weight < d else d
        return d

    def generator_matrix(self, P):
        k = P.size[0]
        I_k = np.identity(k)
        G = np.hstack((I_k, P))
        return G

    def generate_codewords(self, G):
        k, codewords = G.size[0], []
        binary = list(itertools.product([0,1], repeat=k))
        for n in binary:
            codewords.append(np.dot(np.array(n), G))
        return codewords

    def H_matrix(self, P):
        P_T_neg = (-1 * np.transpose(P)) % 2
        I_k = np.identity(len(P_T_neg))
        H = np.hstack((P_T_neg, I_k))
        return H

    def detectable_errors(self, min_Hamming_distance):
        return min_Hamming_distance - 1

    def correctable_errors(self, min_Hamming_distance):
        return (min_Hamming_distance - 1) // 2

    def syndrome(self, P):
        H, syndromes = H_matrix(P), []
        H_T = np.transpose(H)
        binary = list(itertools.product([0,1], repeat=(len(H_T))))
        for n in binary:
            syndromes.append(np.dot(np.array(n), H_T))
        return syndromes
