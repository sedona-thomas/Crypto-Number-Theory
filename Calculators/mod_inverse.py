#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Sedona Thomas
"""

def mod_inverse(k, mod):
    k = k % mod
    i = 1
    while (k * i) % mod != 1:
        i += 1
        if i > mod:
            return -1
    return i
