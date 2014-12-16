import numpy as np

"""
1-funkcija koja od dictionary gradi 1-0 matrica
DONE
2-funkcija koja od adjacency matrix gradi transition matrix
DONE
4-funkcija koja ja inicijalizira raspredelbata
3-funkcija koja implementira power method
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

def transition_matrix(A, df):
    """
        Builds the transition probability matrix for pagerank with restarts,
        A is the adjacency matrix and df is the damping factor
    """
    nodes = A.shape[0]
    Q = np.empty(shape = adj.shape)
    Q.fill(df/nodes)
    row_sums = np.apply_along_axis(sum, 1, adj)
    Q = Q + np.apply_along_axis(normalize, 0, adj, row_sums, df)
    return tm

def normalize(x, sums, df):
    tmp = np.divide(x, sums)
    return np.multiply(tmp, 1-df)

# -----------------------------------------------------------------------------

def power_method(Q):
    """
       Implements the power method for computing page rank with restarts
    """
    # TODO

########################## TEST ##############################
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

    print Q
    print
    print np.apply_along_axis(sum, 1, Q)

main()