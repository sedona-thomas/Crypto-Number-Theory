#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Sedona Thomas
"""

class Hamming(object):

    def Hamming_distance(self, w1, w2):
        w1, w2, d = str(w1), str(w2), 0
        for i in range(len(w1)):
            d += 1 if w1[i] != w2[i] else 0
        return d

    def min_Hamming_distance(self, codes):
        d = len(codes[0])
        for code1 in codes:
            for code2 in codes:
                temp = self.Hamming_distance(code1, code2)
                d = temp if temp < d else d
        return d

