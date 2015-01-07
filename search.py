import pagerank
import numpy as np


def find (word, word_doc):
    """
       Returns list of non-zero (document, word-occurrences) pairs
       for the given word
    """
    occurrences = []
    doc_list = word_doc.get(word, [])

    for pair in doc_list:
        if (pair[1] > 0):
            occurrences.append(pair)

    return occurrences

#------------------------------------------------------------------------------

def find_relevant (occurences, p, urlmap):
    """
        Find relevant documents as function of occurrences and pagerank. Urlmap
        is a dictionary that maps from url to id
    """
    nodes = len(p)
    rank = np.divide(p, (1.0/nodes))          # ratio between the rank of the node and all-equal rank
    for pair in occurences:                   # add to the current rank the number of occurrences of the word
        idx = urlmap[pair[0]]
        rank[idx,0] += pair[1]

    return rank

#------------------------------------------------------------------------------

def sort_rankings (ranking, idmap):
    """
       Sort rankings and map them to url
    """
    result = [(idmap[i], ranking[i,0]) for i in xrange(0, ranking.shape[0])]
    result = sorted(result, key = lambda x: x[1], reverse = True)       # sort by ranks
    return result

#------------------------------------------------------------------------------

def main ():
    wd = {"kniga": [["andrej",0],["verce", 2],["bile", 1],["riste", 3],["magi", 0]],
          "kafe": [["andrej",1],["verce", 3],["bile", 0],["riste", 0],["magi", 2]],
          "parfem": [["andrej",4],["verce", 0],["bile", 2],["riste", 0],["magi", 1]],
          "cokolado": [["andrej",0],["verce", 2],["bile", 0],["riste", 1],["magi", 0]]}

    d = {"verce": ["andrej", "bile", "magi", "vesna"],
         "andrej": ["verce", "buba", "vesna", "tac"],
         "bile": ["riste", "tac", "magi"],
         "magi": ["vesna", "verce", "andrej"],
         "vesna": ["buba"],
         "buba": ["bile", "magi", "tac"],
         "tac": ["riste", "verce", "vesna"],
         "riste" : ["andrej", "bile"]}

    occurrences = find("cokolado", wd)

    # one way
    (idmap, urlmap, A) = pagerank.weighted_adjacency_matrix(d, occurrences)
    Q = pagerank.transition_matrix(A, 0.2);
    p = pagerank.power_method(Q)

    print sort_rankings(p, idmap)

    print
    print

    # another way
    idmap, urlmap, A = pagerank.adjacency_matrix(d)
    Q = pagerank.transition_matrix(A, 0.2);
    p = pagerank.power_method(Q)
    r = find_relevant(occurrences, p, urlmap)

    print sort_rankings(r, idmap)
#------------------------------------------------------------------------------

main()
