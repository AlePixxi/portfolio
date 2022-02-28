#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: alessio
"""
import os

# FUNZIONE CHE RICERCA RICORSIVAMENTE UN FILE NEL FILE SYSTEM
def find_file(directory, name):
    res = []

    for f_name in os.listdir(directory):
        full_path = directory + '/' + f_name

        if os.path.isfile(full_path):
            if full_path.endswith(name):
                res.append(full_path)
        else:
            new_list = find_file(full_path, name)
            res += new_list
    return res


if __name__ == '__main__':
    x = find_file('/home/alessio/log_analysis', 'auth.log')
    print(x)