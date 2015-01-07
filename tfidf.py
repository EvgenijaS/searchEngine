from math import log
import operator
import re

def term_freq (document):
    """
    Calculates term frequency of every word in a document
    document - list of words
    """
    tf = {}
    for word in document:
        count = tf.get(word, 0)
        tf[word] = count + 1

    words_count = 0
    for key in tf:
        words_count += tf[key]

    for key in tf:
        tf[key] = tf[key] / float(words_count)

    return tf


#------------------------------------------------------------------------------

def inverse_doc_freq (documents):
    """
    Calculates inverse document frequency for a set of documents
    documents - is assumed to be a dictionary where each document is mapped
    to a tf dictioanry for all it's words
    """

    docs_per_word = {}
    for doc in documents:
        for word in documents[doc]:
            count = docs_per_word.get(word, 0)
            docs_per_word[word] = count + 1

    idf = {}
    doc_num = float(len(documents))
    for word in docs_per_word:
        idf[word] = log(doc_num / docs_per_word[word])

    return idf


#------------------------------------------------------------------------------

def tf_idf (docs_tf, idf):
    """
    Calculates term frequency * inverse document frequency per document
    given docs_tf and idf as dictionaries, docs_tf is a dictionary in which
    each document is mapped to tf dictionary for it's words'
    """
    tfidf = {}
    for doc in docs_tf:
        tfidf[doc] = {}
        for word in docs_tf[doc]:
            tfidf[doc][word] = docs_tf[doc][word] * idf[word]

    return tfidf


#------------------------------------------------------------------------------

def main ():
    doc1 = "Tf-idf stands for term frequency-inverse document frequency, and the tf-idf weight is a weight often used in information retrieval and text mining. This weight is a statistical measure used to evaluate how important a word is to a document in a collection or corpus. The importance increases proportionally to the number of times a word appears in the document but is offset by the frequency of the word in the corpus."
    doc2 = "Search Engines: Information Retrieval in Practice is ideal for introductory information retrieval courses at the undergraduate and graduate level in computer science, information science and computer engineering departments. It is also a valuable tool for search engine and information retrieval professionals."
    doc3 = "In our much anticipated inaugural episode, Chris and Jonathon talk about the lack of data scientists, sweet big data slides full of 1s and 0s, and visualizations that help you figure out the difference between your third cousin and your first cousin twice removed. Let's roll!"
    doc4 = "For the 12th year running, Google Code Jam returns as one of the top, programming competitions in the world. The contest, which consists of intense algorithmic puzzles held over multiple online rounds culminating in an on-site final round with the top 26 contestants, was bigger than ever last year with nearly 50,000 registrants and our first-ever live streamed finals."
    doc5 = "This may be the wrong place to ask a question, but since I am a newbie an close to desperation I guess you can forgive me. I have the task to build cytoscape from source for a university project. I rigorously followed the instruction to build cytoscape from source(on Windows) and everything seems to work as it should. Cloning the repository and building the core seems flawless but when executing 'cytoscape.sh' it gives the error 'line 80: ./framework/bin/karaf: No such file or directory'"

    doc1 = re.split("[^a-z]", doc1.lower())
    doc2 = re.split("[^a-z]", doc2.lower())
    doc3 = re.split("[^a-z]", doc3.lower())
    doc4 = re.split("[^a-z]", doc4.lower())
    doc5 = re.split("[^a-z]", doc5.lower())

    docs = [doc1, doc2, doc3, doc4, doc5]
    docs_tf = {}
    for i in xrange(5):
        docs_tf[i+1] = term_freq(docs[i])

    idf = inverse_doc_freq(docs_tf)

    tfidf_per_doc = tf_idf(docs_tf, idf)

    for doc in tfidf_per_doc:
        print doc
        sorted_tfidf = [(key,value) for (key, value) in sorted(tfidf_per_doc[doc].items(), key=operator.itemgetter(1), reverse=True)]
        for item in sorted_tfidf:
            print item
        print


#------------------------------------------------------------------------------

main()
