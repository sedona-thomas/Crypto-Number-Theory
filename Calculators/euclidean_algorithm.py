#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Sedona Thomas
"""

class Euclid(object):
    
    # Euclidean Algorithm
    def gcd(self, m, n):
        if m < n:
            m, n = n, m
        r = m % n
        if r > 0:
            print(self.gcd(n, r))
        else:
            print(n)
        
        
    '''
    Returns the GCD of two integers using Euclid's algorithm. Also prints out the
    intermediate steps for Euclid's Algorithm on num1 and num2.
    
    Parameters:
    num1 (int): First number for the GCD
    num2 (int): Second number for the GCD
    
    Returns:
    int: GCD of num1 and num2
    '''
    def euclid(self, a, b):
        
        if abs(a) < abs(b):
            a, b = b, a
        li = [[a,b]]
        r = abs(a)%abs(b)
        while r > 0:
            a, b = abs(b), abs(r)
            li.append([a,b])
            r = abs(a)%abs(b)
        gcd = abs(b)
        
        string = ""
        for x in li:
            string += "GCD(" + str(x[0]) + ", " + str(x[1]) + ") = "
        print(string + str(gcd))
        
        return gcd # your GCD
    
