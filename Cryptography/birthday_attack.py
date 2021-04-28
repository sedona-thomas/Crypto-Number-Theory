#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Sedona Thomas
"""

class BirthdayAttack(object):

    '''
        Birthday Attack on Hash Functions
    '''

    def birthday_attack(self, choices, occurrances):
        x = 1
        for i in range(occurrances):
            x *= (choices - i)
        return 1 - (x / (choices ** occurrances))

