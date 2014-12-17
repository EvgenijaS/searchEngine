#!/usr/bin/python
# -*- coding: utf_8 -*-
import os

def build_word_index (path):
    """
        Builds words index as dictionary of the form word1: [[url1: #occurrences],
        [url2, #occurrences] ...] assuming that for each url we have document
        with all words and their occurrences at location path.
    """
    index = {}
    doc_list = os.listdir(path)
    for doc_name in doc_list:
        path = path + "/" + doc_name           # might need changes for Windows
        doc = open(path, "r")
        for line in doc:
            tokens = line.split()
            index[tokens[0]] = index.get(tokens[0], []) + [doc_name, int(tokens[1])]
        doc.close()

    return index

#------------------------------------------------------------------------------

def main ():
    path = "/home/skyra/Desktop/backup/FINKI/VII-semestar/obrabotka-na-prirodni-jazici/proekt/data"
    index = build_word_index(path)
    print index["октомвриска"]

#------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
