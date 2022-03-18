#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: alessio
"""

import Deck
import time
import random


# INIZIO IL GIOCO, FACCIO SCEGLIERE IL NOME E FACCIO LEGGERE LE REFGOLE
def start():
    print('Benvenuto nel gioco 7 e mezzo! \n'+'-'*40)
    nome_giocatore = input('Con che nome vuoi giocare?: ')
    risposta_regole = input('Vuoi conoscere le regole?: ')
    
    if risposta_regole == 'si'.lower():
        with open('regolamento.txt') as reg:
            for riga in reg:
                print(riga[:-1])
        
        print('\nCOMICNIAMO\n\n'+'-'*40)
            
    else:
        print('Bene allora possiamo cominciare\n\n'+'-'*40)
    
    return nome_giocatore

def carte_coperte(mazzo):
    carte_giocatore = {'nascoste':[], 'visibili': []}
    
    print('\nSTO CONSEGNANDO LE CARTE...')
    time.sleep(1)
    
    carta1 = mazzo.dai_carta()
    carte_giocatore['nascoste'] = carte_giocatore.get('nascoste', [])+[carta1]
    
    return carte_giocatore
    
def giocoBanco(carte, mazzo):
    punteggio_stimato = 0
    carte_banco = []
    punteggio_banco = 0
    
    
    
    for carta in carte: punteggio_stimato += carta.valore
    
    if punteggio_stimato == 0: punteggio_stimato = random.randint(5,6)
    
    while punteggio_banco <= punteggio_stimato:
        carta = mazzo.dai_carta()
        time.sleep(1)
        print(f'Il banco ha pescato {carta.getCarta()}')
        carte_banco.append(carta)
        punteggio_banco += carta.valore
    
    print('\n'+'-'*40)
    time.sleep(1)
    
    return punteggio_banco


    
def main():
    gioco = True
    # DICHIARO LE VARIABILI E INSTANZIO GLI OGGETTI
    mazzo = Deck.Mazzo()
    nome_giocatore = start()
    punteggio_giocatore = 0
    
    mazzo.mischia()
    
    #time.sleep(1)
    carte_giocatore = carte_coperte(mazzo)
    
    #print(carte_giocatore)
    print(f'------ {nome_giocatore} ------') 
    
    print('LE TUE CARTE:', end=' ')
    for carta in carte_giocatore["nascoste"]:
        punteggio_giocatore += carta.valore
        print(carta.getCarta(), end=' ')
    
    print(f'\nIL TUO PUNTEGGIO È: {punteggio_giocatore}')
    
    # INIZIO DEL GAME LOOP
    while gioco:
        time.sleep(4)
        print('\n'+'-'*40)
        
        if punteggio_giocatore > 7.5: 
            print('HAI SBALLATO! PARTITA TERMINATA')
            gioco = False
            break
        
        risp = input("'carta' per ricevere una carta, \n'sto' per fermarti \n'punteggio' per vedere le carte e il punteggio: ")
        
        if risp.lower() == 'carta':
            print('\n\t CONSEGNO LA CARTA...')
            time.sleep(1)
            
            carta = mazzo.dai_carta()
            carte_giocatore['visibili'] = \
                carte_giocatore.get('visibili', [])+[carta]
                
            punteggio_giocatore += carta.valore
            time.sleep(1)
            print(f'hai pescato {carta.getCarta()}')
            
        elif risp.lower() == 'sto' : gioco = False
        elif risp.lower () == 'punteggio':
            for lista_carte in carte_giocatore.values():
                if len(lista_carte) > 0:
                    for carta in lista_carte:
                        print(carta.getCarta())
            print(f'Il tuo attuale punteggio è: {punteggio_giocatore}')             
            
            
    # FUORI DAL GAME LOOP    
    print('\n'+'-'*40)    
    print(f'hai terminato con {punteggio_giocatore} punti')
    time.sleep(1)
    
    if punteggio_giocatore <= 7.5:
        print('Ora stiamo a vedere il banco...')
        time.sleep(1)
        carte_conosciute = carte_giocatore['visibili']

        punteggio_banco = giocoBanco(carte_conosciute, mazzo)
        print(f'il banco ha realizzato {punteggio_banco} punti')
        
        if punteggio_banco > 7.5:
            print('\n'+'-'*40)
            print('Il banco ha sballato, HAI VINTO!')
            
        elif punteggio_banco >= punteggio_giocatore: 
            print('\n'+'-'*40)
            print('''Il banco ha fatto più punti, HAI PERSO!''')
        
        
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    