#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: alessio
"""

import file_finder
import csv


# eseguo la funzione che ricerca nel file sistem il file che mi serve
def find_path(directory, name):
    file = file_finder.find_file(directory, name)
    return file[0]

# leggo il file di log e lo rielaboro
def read_log(file_path):
    l = []
    with open(file_path) as fl:
        for row in fl:
            _ = row.split()
            l.append(_)
    return l

# salvo tutte le classi presenti nel log
def classes(file):
    dict_classes = {}
    
    for log in file:
        dict_classes[log[2]] = dict_classes.get(log[2], 0)+1
    ordered = sorted(dict_classes.items(), key = lambda x : x[0])
    
    return ordered

# salvo tutte le gravità di log e registro quante volte vengono chiamate
def types(m_file):
    list_types = {}
    
    for row in m_file:
        list_types[row[3]] = list_types.get(row[3], 0)+1
    
    return sorted(list_types.items(), key = lambda x : x[1], reverse=True )

# creo un resoconto dell'analisi e lo salvo in un file di testo
def result(list_classes, list_types):
    to_write = 'Sono state trovate le seguenti classi:\n\n'
    n = 40
    
    tot = sum(list(map(lambda x : x[1], list_classes)))
    
    for class_ in list_classes:
        text = f'\t- {class_[0]} per {class_[1]} volte\n'
        to_write += text
        
    to_write += f'\nPer un totale di {tot} log registrati\n'
    to_write += '_'*n + '\n'
    to_write += '\nSono state registrate le seguenti tipologie di log:\n\n'
    
    for type_ in list_types:
        text_types = f'\t- {type_[0]} per un totale di {type_[1]} volte\n'
        to_write += text_types
        
    with open('info.txt', 'w') as fs:
        fs.write(to_write)

# creo un file csv e registro le informazioni principali dei log
def write_csv(m_file, ording=0):
    with open('output.csv', 'w') as csvfile:
        l = []
        title_writer = csv.writer(csvfile)
        title_writer.writerow(['DATA', 'TIPO', 'CLASSE', 'ID'] )
        content_writer = csv.writer(csvfile)
        
        for row in m_file:
            date = [' '.join(row[:2])]
            class_ = [row[2]]
            type_ = [row[3]]
            id_ = [str(row[-1])]
            list_temp = date+class_+type_+id_
            
            l.append(list_temp)
            
        content_writer.writerows(sorted(l, key=lambda x : x[ording]))
            
# funzione principale del programma
def main(directory, name):
    
    file_path = find_path(directory, name)
    
    m_file = read_log(file_path)

    list_classes = classes(m_file)
    list_types = types(m_file)
    
    result(list_classes, list_types)
    write_csv(m_file)
    
    
# eseguo il codice
if __name__ == '__main__':
    main('.', 'sample.log')
