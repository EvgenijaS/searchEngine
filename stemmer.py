# -*- coding: utf-8 -*-

class Node:

    def __init__(self, letter = '#', parent = None):
        self.children = {}
        self.count = 0          # number of words that contain the prefix
        self.letter = letter
        self.parent = parent
        self.full_word = False  # completes a word


    def add (self, word):
        """ Add word """
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
        """ Get the word (prefix) that ends at the current node"""
        word = ''
        node = self
        while node.letter != '#':
            word += node.letter
            node = node.parent
        word = word[::-1]
        return word


    def peak_and_plateau (self, word, idx = 0):
        """ Peak-and-plateau stemming implementation """
        # if root
        if self.letter == '#':
            return self.children[word[0]].peak_and_plateau(word, idx)
        # otherwise
        else:
            if (len(word) == idx+1):                           # if at the end of a word
                return self.get_word()

            prev_sv = len(self.parent.children)                # successor variety of the parent
            sv = len(self.children)                            # successor variety of the current node
            next_sv = len(self.children[word[idx+1]].children) # successor variety of the child-node that follows

            if sv > prev_sv and sv >= next_sv and idx > 1:     # sudden growth of sv and at least third letter in word
                  return self.get_word()
            else:                                              # otherwise continue with the next letter
                return self.children[word[idx+1]].peak_and_plateau(word, idx+1)


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
        """ Add word to the trie """
        if len(word) > 0:
            self.root.add(word)

    def find_stem(self, word):
        """ Find stem of a word, after the trie is built"""
        return self.root.peak_and_plateau(word, 0)

    def __str__ (self):
        return self.root.__str__()


###############################################################################
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

    print "The Trie is built"

    # remove sufixes
    stems = []
    redo_words = []
    for word in words:
        if len(word) > 3:
            stem = word[::-1].replace(trie_reversed.find_stem(word[::-1]), '', 1)[::-1]
            if len(stem) < 3:
                redo_words.append(word)
            else:
                stems.append((stem, word))
                #redo_words.append(stem)


    # find word root
    for word in redo_words:
        if len(word) > 3:
            stem = trie.find_stem(word)
            stems.append((stem, word))


    for s in stems:
        print 'WORD: ' + s[1]
        print 'STEM: ' + s[0]
        print


    fw = open("../../data/stems.txt", "w")
    fw.write(str(sorted([i[0] for i in stems])))
    fw.close()

    fw = open("../../data/stems-word-pairs.txt", "w")
    fw.write(str(sorted(stems)))
    fw.close()


if __name__ == '__main__':
    main()
