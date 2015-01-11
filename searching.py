# -*- coding: utf-8 -*-
import numpy as np
import re
import tfidf
import operator


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
    documents_tf_idf = [get_document(url) for url in urls]

    # get pageranks
    pageranks = [get_pagerank('url') for url in urls]

    # query to tf-idf vector
    query_tf_idf = np.zeros(shape = documents_tf_idf.shape)
    stems_tf = tfidf.tf()              # tf of the stems
    for stem in query_stems:
        query_tf_idf[get_word_index(stem)] = stems_tf.get(stem, 0) * get_word_idf(stem)

    # calculate the score for each document
    score = [(1 - c)*cosine_similarity(query_tf_idf, doc) for doc in documents_tf_idf]
    score = score + c * pageranks

    # sort documents by score
    result = dict(zip(urls, score))

    return sorted(result.items(), key=operator.itemgetter(1), reverse=True)

#-------------------------------------------------------------------------------

def cosine_similarity(v1, v2):
    v1_norm = np.linalg.norm(v1)
    v2_norm = np.linalg.norm(v2)
    dot_product = np.dot(v1, v2)
    return float(dot_product) / (v1_norm*v2_norm)


###############################################################################
#-----------------TEST----------------------------------------------------------

def main():
    query = u'Факултет за информатика и компјутерско инженерство'
    res = search(query)

    print res



if __name__ == '__main__':
    main()