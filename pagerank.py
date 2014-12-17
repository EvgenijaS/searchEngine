import numpy as np

"""
4-funkcija koja go sortira pagerankot
"""

def adjacency_matrix(links):
    """
       Builds adjacency matrix form a dictionary that maps URL to list
       of URL's it links to. Also returns dictionary that maps ID to URL
    """
    id_to_url = {}
    url_to_id = {}
    i = 0
    for url in links.keys():
        id_to_url[i] = url
        url_to_id[url] = i
        i += 1

    A = np.zeros(shape = (len(links),len(links)))
    for url in links.keys():
        for link in links[url]:
            A[url_to_id[url], url_to_id[link]] = 1

    return id_to_url, A

#------------------------------------------------------------------------------

def weighted_adjacency_matrix(links, occurrences):
    """
       Builds weighted adjacency matrix form a dictionary that maps URL to list
       of URL's it links to. Also returns dictionary that maps ID to URL.
       Occurrences is a list of tuples of documents and number of occurrences
       for the searched word. Links pointing to documents in this list have
       larger weight
    """
    id_to_url = {}
    url_to_id = {}
    i = 0
    for url in links.keys():
        id_to_url[i] = url
        url_to_id[url] = i
        i += 1

    A = np.zeros(shape = (len(links),len(links)))
    for url in links.keys():
        for link in links[url]:
            A[url_to_id[url], url_to_id[link]] = 1

    # add the weigths
    nodes = A.shape[0]
    for pair in occurrences:
        idx = url_to_id[pair[0]]
        for i in xrange(nodes):
            if A[i, idx] == 1:
                A[i, idx] = 2 ** pair[1]  # weighted exponentialy according
                                          # to the number of occurences of the
                                          # word
    return id_to_url, A

#------------------------------------------------------------------------------

def transition_matrix(A, df):
    """
        Builds the transition probability matrix for pagerank with restarts,
        A is the adjacency matrix and df is the damping factor
    """
    nodes = A.shape[0]
    Q = np.empty(shape = A.shape)
    Q.fill(df/nodes)
    row_sums = np.apply_along_axis(sum, 1, A)
    Q = Q + np.apply_along_axis(normalize, 0, A, row_sums, df)
    return Q

def normalize(x, sums, df):
    tmp = np.divide(x, sums)
    return np.multiply(tmp, 1-df)

# -----------------------------------------------------------------------------

def power_method(Q):
    """
       Implements the power method for computing page rank with restarts
    """
    nodes = Q.shape[0]
    p = np.empty((nodes, 1))
    p.fill(1.0/nodes)
    Q = np.transpose(Q)

    old_p = np.zeros(p.shape)
    while np.sum(np.absolute(old_p - p)) > 10e-5:
        old_p = np.copy(p)
        p = np.dot(Q, p)

    return p

#------------------------------------------------------------------------------

########################## TEST ##############################
"""
def main ():
    d = {"verce": ["andrej", "bile", "magi", "vesna"],
         "andrej": ["verce", "buba", "vesna", "tac"],
         "bile": ["riste", "tac", "magi"],
         "magi": ["vesna", "verce", "andrej"],
         "vesna": ["buba"],
         "buba": ["bile", "magi", "tac"],
         "tac": ["riste", "verce", "vesna"],
         "riste" : ["andrej", "bile"]}

    idmap, A = adjacency_matrix(d)
    Q = transition_matrix(A, 0.2);
    p = power_method(Q)

    print idmap
    print
    print p


main()
"""