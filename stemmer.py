# -*- coding: utf-8 -*-

class Node:

    def __init__(self, letter = '#', parent = None):
        self.children = {}
        self.count = 0          # number of word that begin with
        self.letter = letter
        self.parent = parent
        self.full_word = False  # completes a word


    def add (self, word):
        self.count += 1
        # if root
        if self.letter == '#':
            if word[0] not in self.children:
                self.children[word[0]] = Node(word[0], self)
            self.children[word[0]].add(word)
        # if not root
        else:
            if len(word) == 1:
                self.full_word = True
            else:
                if word[1] not in self.children:
                    self.children[word[1]] = Node(word[1], self)
                self.children[word[1]].add(word[1:])


    def get_word (self):
        if self.letter == '#':
            return ''
        word = ''
        node = self
        while node.letter != '#':
            word += node.letter
            node = node.parent
        word = word[::-1]
        return word

    """
    def stem_search (self, word):
        # parameters to fit
        GRANKI = 2
        DO_TUKA = 3

        # if root
        if self.letter == '#':
            return self.children[word[0]].stem_search(word)
        # otherwise
        else:
            #prev_count = len(self.parent.children)
            #next_count = 0
            #if len(word) > 1:
            #    next_count = len(self.children[word[1]].children)
            self_count = len(self.children)

            if (len(word) == 1) or (self_count >= GRANKI and self.count <= DO_TUKA): #(next_count == 0) or (self_count > prev_count and self_count > next_count):
                return self.get_word()
            else:
                return self.children[word[1]].stem_search(word[1:])
    """


    def stem_search (self, word, idx = 0):
        # if root
        if self.letter == '#':
            return self.children[word[0]].stem_search(word, idx)
        # otherwise
        else:
            if (len(word) == idx+1):
                return self.get_word()

            prev_sv = len(self.parent.children)
            sv = len(self.children)    # current successor variety
            next_sv = len(self.children[word[idx+1]].children)

            if sv > prev_sv and sv >= next_sv and idx > 1:  # suddent growth of sv and atleast third letter in word
                  return self.get_word()
            else:
                return self.children[word[idx+1]].stem_search(word, idx+1)


    def __str__ (self):
        s = self.letter + '-' + str(self.count) + '\n'
        for child in self.children:
            s += child
            s += ' '
        s += '\n'

        for child in self.children:
            s += self.children[child].__str__()
        return s



class Trie:

    def __init__(self):
        self.root = Node()

    def add_word (self, word):
        if len(word) > 0:
            self.root.add(word)

    def find_stem(self, word):
        return self.root.stem_search(word, 0)

    def __str__ (self):
        return self.root.__str__()


#------------------TEST--------------------------------------------------------
import re

def main ():
    trie = Trie()
    trie_reversed = Trie()

    f = open('../../data/words.txt', 'r')
    text = u"" + f.read().decode('utf-8')
    f.close()

    #words = set(re.findall(ur"(?u)\w+", text.lower()))
    words = eval(text)

    for word in words:
        trie.add_word(word)

    for word in words:
        trie_reversed.add_word(word[::-1])


    # remove sufixes
    stems = []
    redo_words = []
    for word in words:
        if len(word) > 3:
            stem = word[::-1].replace(trie_reversed.find_stem(word[::-1]), '', 1)[::-1]  # ja naogjame nastavkata namesto zborot i ja trgame
            if len(stem) < 3:
                redo_words.append(word)
            else:
                stems.append((word, stem))
                #redo_words.append(stem)


    # find word root
    for word in redo_words:
        if len(word) > 3:
            stem = trie.find_stem(word)
            stems.append((word, stem))


    for s in stems:
        print 'WORD: ' + s[0]
        print 'STEM: ' + s[1]
        print

###############################################################################

if __name__ == '__main__':
    main()
