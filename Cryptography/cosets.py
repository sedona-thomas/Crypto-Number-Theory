#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Sedona Thomas
"""

class Cosets(object):

    def elements_in_coset(self, n, k):
        return 2**k

    def number_of_cosets(self, n, k):
        return 2**(n-k)
