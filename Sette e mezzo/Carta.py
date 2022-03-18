#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: alessio
"""

class Carta:
    def __init__(self, numero, seme, valore):
        self.seme = seme
        self.numero = numero
        self.valore = valore
        
    def getCarta(self):
        return self.numero, self.seme