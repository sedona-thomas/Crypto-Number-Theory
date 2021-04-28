#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Sedona Thomas
"""

import math

class EllipticCurve(object):

    def elliptic_curve_finder(self, b, c, m):
        for x in range(m):
            y = self.elliptic_curve_x(x, b, c, m)**2
            while math.sqrt(y) < m:
                if math.sqrt(y) % 1 == 0:
                    print(x, math.sqrt(y))
                y += m
        print("∞")

    def elliptic_curve_x(self, x, b, c, m):
        return math.sqrt((x**3 + b*x + c) % m)

    def add_elliptic_curve(self, x1, y1, x2, y2, b, c, m):
        if (x1, y1) == (x2, y2):
            return self.add_elliptic_curve_eq(x1, y1, b, c, m)
        else:
            return self.add_elliptic_curve_ne(x1, y1, x2, y2, b, c, m)
        
    def add_elliptic_curve_eq(self, x, y, b, c, mod):
        s = ""
        a1, a2 = 3 * (x**2) + b, self.mod_inverse(2*y, mod)
        m = (a1 * a2) % mod
        temp = "m = (3 * {}^2 + {}) * (2*{})^-1 mod {} = {} * {} mod {} = {}\n"
        s += temp.format(x, b, y, mod, a1, a2, mod, m)
        x3 = (m**2 - x - x) % mod
        y3 = (m*(x - x3) - y) % mod
        s += "x3 = ({}^2 - {} - {}) mod {} = {}\n".format(m, x, x, mod, x3)
        s += "y3 = ({}({} - {}) - {}) mod {} = {}\n".format(m, x, x3, y, mod, y3)
        print(s)
        return x3, y3

    def add_elliptic_curve_ne(self, x1, y1, x2, y2, b, c, mod):
        s = ""
        a1, a2 = (y2-y1), self.mod_inverse(x2-x1, mod)
        m = (a1 * a2) % mod
        temp = "m = ({} - {}) * ({} - {})^-1 % {} = {} * {} mod {} = {}\n"
        s += temp.format(y2, y1, x2, x1, mod, a1, a2, mod, m)
        x3 = (m**2 - x1 - x2) % mod
        y3 = (m*(x1 - x3) - y1) % mod
        s += "x3 = ({}^2 - {} - {}) mod {} = {}\n".format(m, x1, x2, mod, x3)
        s += "y3 = ({}({} - {}) - {}) mod {} = {}\n".format(m, x1, x3, y1, mod, y3)
        print(s)
        return x3, y3

    def repeat_elliptic_curve(self, k, x, y, b, c, m):
        j, x1, y1, x2, y2 = k, x, y, x, y
        while (j > 0):
            x1, y1 = self.add_elliptic_curve(x1, y1, x2, y2, b, c, m)
            j -= 1
        print("efficient:")
        i, x1, y1 = 2, x, y
        while (k - i > 0):
            x1, y1 = self.add_elliptic_curve(x1, y1, x1, y1, b, c, m)
            k, i = k - i, i * 2
        while (k > 0):
            x1, y1 = self.add_elliptic_curve(x1, y1, x, y, b, c, m)
            k -= 1

    def mod_inverse(self, k, mod):
        if k == 0:
            print("ERROR: k cannot equal 0")
        x = k % mod
        for i in range(1, mod):
            if ((x * i) % mod == 1):
                s = "{}d = 1 + {}x = 1 + ({} × {}) = 1 + {} = {}"
                print(s.format(k, mod, mod, (k*i - 1)//mod, k*i - 1, k*i))
                print("d = {}".format(i))
                return i
        return 1

