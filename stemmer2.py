#!/usr/bin/python
# -*- coding: utf-8 -*-

def build_stems_dictionary (filename):
    """
    Reads in the supplied stems file and builds
    dictionary that maps from word to stem
    """
    word_to_stem = {}
    with open(filename, 'r') as stems_file:
        for line in stems_file:
            tokens = line.decode('utf-8').rstrip().split()
            word_to_stem[tokens[0]] = tokens[1]

    return word_to_stem



###############################################################################
#-----------------TEST----------------------------------------------------------

def main ():
    d = build_stems_dictionary('../../data/stems_dictionary.tbl')
    print d.get('екстерната'.decode('utf-8'), None)
    print d.get('своите'.decode('utf-8'), None)
    print d.get('подигнување'.decode('utf-8'), None)
    print d.get('верификација'.decode('utf-8'), None)


if __name__ == '__main__':
    main()
