
#-------------------------------------------------------------------------
# AUTHOR: Bryan Martinez Ramirez
# FILENAME: indexing.py
# SPECIFICATION: Indexing words with given collection of documents
# FOR: CS 4250- Assignment #1
# TIME SPENT: 2 hours
#-----------------------------------------------------------*/
#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH
#AS numpy OR pandas. You have to work here only with standard arrays
# Importing some Python libraries
import csv
import math #import math for log

# Reading the data in a csv file
documents = []
with open('collection.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            documents.append(row[0])

# Conducting stopword removal. 
stopWords = {'i', 'and', 'the', 'is', 'she', 'he', 'they', 'her', 'their'}
# Conducting stemming. 
stemming = {'loves': 'love', 'cats': 'cat', 'dogs': 'dog'}

# Identifying the index terms.
terms = set()
for doc in documents:
    words = doc.lower().split()
    for word in words:
        if word not in stopWords:
            stemmed_word = stemming.get(word, word)
            terms.add(stemmed_word)
# Sort the terms for consistent ordering
terms = sorted(list(terms))

# Building the df matrix by using the tf-idf weights.
def tf(term, doc):
    return doc.lower().split().count(term.lower())

def idf(term, documents):
    num_docs_with_term = sum(1 for doc in documents if term in doc.lower().split())
    return math.log(len(documents) / (1 + num_docs_with_term))

docTermMatrix = []
for doc in documents:
    row = []
    for term in terms:
        row.append(tf(term, doc) * idf(term, documents))
    docTermMatrix.append(row)

# Printing the df matrix.
for row in docTermMatrix:
    print(row)
