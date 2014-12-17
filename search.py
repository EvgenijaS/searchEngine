import pagerank


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



def main ():
    wd = {"kniga": [("andrej",0),("verce", 2),("bile", 1),("riste", 3),("magi", 0)],
          "kafe": [("andrej",1),("verce", 3),("bile", 0),("riste", 0),("magi", 2)],
          "parfem": [("andrej",4),("verce", 0),("bile", 2),("riste", 0),("magi", 1)],
          "cokolado": [("andrej",0),("verce", 2),("bile", 0),("riste", 1),("magi", 0)]}

    d = {"verce": ["andrej", "bile", "magi", "vesna"],
         "andrej": ["verce", "buba", "vesna", "tac"],
         "bile": ["riste", "tac", "magi"],
         "magi": ["vesna", "verce", "andrej"],
         "vesna": ["buba"],
         "buba": ["bile", "magi", "tac"],
         "tac": ["riste", "verce", "vesna"],
         "riste" : ["andrej", "bile"]}

    occurrences = find("parfem", wd)
    # idmap, A = pagerank.adjacency_matrix(d)
    idmap, A = pagerank.weighted_adjacency_matrix(d, occurrences)
    print A
    print
    print

    Q = pagerank.transition_matrix(A, 0.2);
    p = pagerank.power_method(Q)

    print idmap
    print
    print p

#------------------------------------------------------------------------------

main()
