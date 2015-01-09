# -*- coding: utf_8 -*-

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


    def stem_search (self, word, prev_sv):
        # if root
        if self.letter == '#':
            return self.children[word[0]].stem_search(word, len(self.children))
        # otherwise
        else:
            sv = len(self.children)    # current successor variety

            if (len(word) == 1) or (sv > prev_sv and self.parent != None and self.parent.parent != None):  # suddent growth of sv and atleast third letter in word
                  return self.get_word()
            else:
                return self.children[word[1]].stem_search(word[1:], sv)


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

    text = 'Stemming removes word suffixes, perhaps recursively in layer after layer of processing. The process has two goals. In terms of efficiency, stemming reduces the number of unique words in the index, which in turn reduces the storage space required for the index and speeds up the search process. In terms of effectiveness, stemming improves recall by reducing all forms of the word to a base or stemmed form. For example, if a user asks for analyze, they may also want documents which contain analysis, analyzing, analyzer, analyzes, and analyzed. Therefore, the document processor stems document terms to analy- so that documents which include various forms of analy- will have equal likelihood of being retrieved; this would not occur if the engine only indexed variant forms separately and required the user to enter all. Of course, stemming does have a downside. It may negatively affect precision in that all forms of a stem will match, when, in fact, a successful query for the user would have come from matching only the word form actually used in the query. Milosevic\'s comments, carried by the official news agency Tanjug, cast doubt over the governments at the talks, which the international community has called to try to prevent an all-out war in the Serbian province. "President Milosevic said it was well known that Serbia and Yugoslavia were firmly committed to resolving problems in Kosovo, which is an integral part of Serbia, peacefully in Serbia with the participation of the representatives of all ethnic communities," Tanjug said. Milosevic was speaking during a meeting with British Foreign Secretary Robin Cook, who delivered an ultimatum to attend negotiations in a week\'s time on an autonomy proposal for Kosovo with ethnic Albanian leaders from the province. Cook earlier told a conference that Milosevic had agreed to study the proposal. While essential and potentially important in affecting the outcome of a search, these first three steps simply standardize the multiple formats encountered when deriving documents from various providers or handling various Web sites. The steps serve to merge all the data into a single consistent data structure that all the downstream processes can handle. The need for a well-formed, consistent format is of relative importance in direct proportion to the sophistication of later steps of document processing. Step two is important because the pointers stored in the inverted file will enable a system to retrieve various sized units — either site, page, document, section, paragraph, or sentence.'
    words = set(re.split("[^a-z]", text.lower()))
    for word in words:
        trie.add_word(word)
    #print trie
    print 'OK'

    for word in words:
        if len(word) > 0:
            print 'WORD: ' +  word
            print 'STEM: ' + trie.find_stem(word)
            print

if __name__ == '__main__':
    main()
