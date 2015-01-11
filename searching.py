# -*- coding: utf-8 -*-
import numpy as np
import re
import tfidf
import operator
import math


def get_match(word):
    #TODO
    return ['url1', 'url2', 'url3']

def get_document(url):
    #TODO
    return 'tf-idf representation'

def get_pagerank(url):
    #TODO
    return 'Pagerank'

def get_word_index(word):
    #TODO
    return 0

def get_word_idf(word):
    #TODO
    return 0.5


#-------------------------------------------------------------------------------

c = 0.3  # rank relevance tradeoff

#-------------------------------------------------------------------------------

def search(query):
    """
       Return list relevant documents given the query as string
    """
    tokens = set(re.findall(ur"(?u)\w+", query.lower().decode('utf-8')))     # split on non-alpha character

    #TODO remove stop words

    # get relevant documents
    urls = []
    query_stems = []
    for t in tokens:
        term = t
        res = get_match(term)
        while term and res == None:
            term = term[:-1]
            res = get_match(term)
        urls.extend(res)
        query_stems.append(term)

    # get document vectors (tf-idfrepresentation)
    documents_tf_idf = [get_document(url) for url in urls]        # list of dictionaries

    # get pageranks
    pageranks = [get_pagerank('url') for url in urls]

    # query to tf-idf vector
    stems_tfidf = tfidf.term_freq(query_stems)                    # tf of the stems (dictionary)
    for stem in query_stems:
        stems_tfidf[stem] *= get_word_idf(stem)

    # calculate the score for each document
    score = [(1 - c)*cosine_similarity(stems_tfidf, documents_tf_idf[doc]) for doc in documents_tf_idf]
    score = score + c * pageranks

    # sort documents by score
    result = dict(zip(urls, score))

    return sorted(result.items(), key=operator.itemgetter(1), reverse=True)

#-------------------------------------------------------------------------------

def cosine_similarity(query, doc):
    """ Both query and doc are dictionaries stem - tfidf """
    cos = 0
    for stem in query:
        if stem in doc:
            cos += (query[stem] * doc[stem])

    m1 = vector_magnitude(query)
    m2 = vector_magnitude(doc)

    cos /= float(m1*m2)
    return cos


def vector_magnitude(v):
    """ v is considered to be dictionary stem-tfidf"""
    m = 0
    for stem in v:
        m += v[stem]**2
    return math.sqrt(m)



###############################################################################
#-----------------TEST----------------------------------------------------------

def main():
    query = u'Факултет за информатика и компјутерско инженерство'
    res = search(query)

    print res



if __name__ == '__main__':
    main()