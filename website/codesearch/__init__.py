import pandas as pd
import numpy as np
import re
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
default_app_config = 'codesearch.apps.CodesearchConfig'
print("server initialization starts")

ROOT_DIR='D:\\BigData_StackOverflowQuery-master\\website\\'
DIC_DIR=''

# set up the system for starting the service
# this needs some time and large enough RAM (8GB RAM is big enough)
# lookup dictionary named embeddings_index will exist in the RAM until the program is shut down
def sys_prepare():
    print("Preparing word vector dictionary")
    e={}
    with open(
            r'E:\NLP\spooky\glove.840B.300d.txt',
            encoding="utf-8") as f:
        for line in f:
            values = line.split()
            word = values[0]
            try:
                coefs = np.asarray(values[1:], dtype='float32')
            except:
                continue
            e[word] = coefs
    return e

# param: a string value representing the query string
# return a list of strings representing searching keywords
def clean(query):
    if not type(query) == str:
        query = str(query)
    query = query.lower()
    query = re.sub(r"[^A-Za-z^]", " ", query)
    rt = query.split()
    rt = [x for x in rt if x not in stop_words and x != 'python']
    if not rt:
        return query.split(" ")
    rt = [lem.lemmatize(x) for x in rt]
    return rt


# param: a list of strings representing the paragraph to be vectorized
# return: a 300 dimensional vector(list) of type double representing the vectorized paragraph
def vectorize(x):
    rt = np.zeros(300)
    for i in x:
        try:
            rt += embeddings_index[i]
        except:
            continue
    rt /= len(x)
    return rt


# Singleton utility
# We load them here to avoid multiple instantiation across other
# modules, that would take too much time.
print('system setup time starts')
df = pd.read_csv(ROOT_DIR+'codesearch\\QA.csv', encoding='iso-8859-1')
embeddings_index=sys_prepare()
stemmer = PorterStemmer()
lem = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))
df['Title_cleaned'] = df['Title'].apply(clean)
df['Title_vector'] = df['Title_cleaned'].apply(vectorize)
print("server setup time finishes")


