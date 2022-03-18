#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: alessio
"""

import Carta
import random

class Mazzo:
    def __init__(self):
        
        self.n_carte = 10
        self.semi = ['Spade', 'Denari', 'Bastoni', 'Coppe']
        self.mazzo = []
        valore = 0
        
        for i, s in enumerate(self.semi):
            for n in range(1, self.n_carte+1):
                
                if n > 7: valore = 0.5 
                else: valore = n 
                
                carta = Carta.Carta(n, s, valore)
                self.mazzo.append(carta)
    
    def get_mazzo(self):
        return self.mazzo
    
    def mischia(self):
        random.shuffle(self.mazzo)
    
    def dai_carta(self):
        carta_da_consegnare = self.mazzo[0]
        self.mazzo.pop(0)
        return carta_da_consegnare
