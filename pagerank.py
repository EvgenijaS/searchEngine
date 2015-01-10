import numpy as np
import operator
import json

"""
4-funkcija koja go sortira pagerankot
"""

def adjacency_matrix(links):
    """
       Builds adjacency matrix from a dictionary that maps URL to list
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

    return id_to_url, url_to_id, A

#------------------------------------------------------------------------------

def transition_matrix(A, df):
    """
        Builds the transition probability matrix for pagerank with restarts,
        A is the adjacency matrix and df is the damping factor
    """
    nodes = A.shape[0]

    A = A + 10e-20
    row_sums = A.sum(axis = 1)
    Q = A / row_sums[:, np.newaxis]
    Q = Q * (1-df)
    Q = Q + (df/nodes)

    return Q

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

    return np.array(p.transpose()[0])

#-------------------------------------------------------------------------------

def pagerank(graph, damping_factor):
    """
       Calculates the pagerank given the graph as dictionary where url maps to
       list of urls and damping factor
    """
    id_map, url_map, A = adjacency_matrix(graph)
    Q = transition_matrix(A, damping_factor)
    p = power_method(Q)
    print p.sum()
    urls = [id_map[i] for i in xrange(0,len(url_map))]
    rank = dict(zip(urls, p))

    return rank

###############################################################################
#---------------------------TEST------------------------------------------------

def main ():
    file_reader = open('../../data/graph.txt', 'r')
    graph_str = file_reader.read()
    graph = eval(graph_str)

    file_writer = open('../../data/graph.json', 'w')
    file_writer.write(json.dumps(graph))
    file_writer.close()

    p = pagerank(graph, 0.15)
    sorted_ranks = sorted(p.items(), key=operator.itemgetter(1), reverse=True)
    print sorted_ranks
    file_writer = open('../../data/pageranks_sorted.txt', 'w')
    file_writer.write(str(sorted_ranks))
    file_writer.close()

    file_writer = open('../../data/pageranks.txt', 'w')
    file_writer.write(str(p))
    file_writer.close()



if __name__ == '__main__':
    main()