# include packages in need
# for nltk stopwords, the corresponding corpuses need to be downloaded first hand

from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
import os
import re
import numpy as np
import pandas as pd
from tqdm import tqdm

# change the directory to where you put this program as well as two raw datasets
os.chdir(r"C:\cs4266\BigData_StackOverflowQuery\website\codesearch")
stop_words = set(stopwords.words('english'))
# word stemmer and lemmatizer
stemmer = PorterStemmer()
lem = WordNetLemmatizer()
embeddings_index = {}


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


# set up the system for first time running on this machine
# Questions.csv, Answers.csv and glove.840B.300d.txt(word vector representation) need to be downloaded
# ahead of time and put in the same folder as this program
# optimized dataset named "QA.csv" will be created in the working directory
def sys_setup():
    print("Setting up the system for first time running...")
    dfq = pd.read_csv('Questions.csv', encoding='iso-8859-1')
    dfa = pd.read_csv('Answers.csv', encoding='iso-8859-1')
    dft = pd.read_csv('Tags.csv', encoding='iso-8859-1')
    tgroup = dft.groupby('Id')['Tag'].apply(list)
    tgroup = tgroup.to_frame()
    tgroup['Id'] = tgroup.index

    dfq_full = pd.merge(dfq, tgroup, on='Id', how='outer')
    dfq_full.sort_values(['Score', 'CreationDate'], ascending=[False, False], inplace=True)

    dfa.sort_values(['Score', 'CreationDate'], ascending=[False, False], inplace=True)
    dfqa = pd.merge(dfq_full, dfa, left_on='Id', right_on='ParentId', how='left')
    dfqa.to_csv("QA.csv", encoding='iso-8859-1')


# set up the system for starting the service
# this needs some time and large enough RAM (8GB RAM is big enough)
# lookup dictionary named embeddings_index will exist in the RAM until the program is shut down
def sys_prepare():
    print("Preparing the query system...")
    with open(
            r'C:\cs4266\BigData_StackOverflowQuery\website\codesearch\glove.840B.300d.txt',
            encoding="utf-8") as f:
        for line in tqdm(f):
            values = line.split()
            word = values[0]
            try:
                coefs = np.asarray(values[1:], dtype='float32')
            except:
                continue
            embeddings_index[word] = coefs


# params: two vectors(lists of type double)
# return: the distance between vectors(lists of type double)
def distance(first, second):
    return np.sum((first - second) ** 2)


# param: a reference to current row in the dataframe
# print out the answer in a pretty format
def fetch_answer(r):
    print('######## answer to question ########')
    print("### score ", r['Score_y'], " ###")
    soup = BeautifulSoup(r['Body_y'], "html.parser")
    tags = soup.find_all('code')
    result = ""
    for i in tags:
        result += i.text
        result += '\n'
    print(result)


# param: a reference to current row in the dataframe
# return: a formatted string of the answer
def fetch_answer_for_web(r):
    s = '######## answer to question ########<br>'
    s += "### score " + str(r['Score_y']) + " ###<br>"
    soup = BeautifulSoup(r['Body_y'], "html.parser")
    tags = soup.find_all('code')
    result = ""
    for i in tags:
        result += i.text
        result += '<br>'
    s += result
    return s


# param: the query that the user entered
# return: the formatted results of the search
def run_program(q):
    # preparing the system
    sys_prepare()
    if not os.path.exists("QA.csv"):
        sys_setup()

    # read in the optimized dataset
    print('Finding results...')
    df = pd.read_csv('QA.csv', encoding='iso-8859-1')
    df['Title_cleaned'] = df['Title'].apply(clean)
    df['Title_vector'] = df['Title_cleaned'].apply(vectorize)

    query = q
    query = clean(query)  # clean the query
    query = vectorize(query)  # vectorize the query

    # the string answer to return
    s = ""
    # the max distance to mark if two vectors are 'similar'
    bottleneck = 12
    # number of questions in the dataset to find
    count = 3
    # number of answers to fetch for each question found
    subcount = 3
    tmpid = None
    # after dataframe join: column naming convention: _x for question and _y for answer
    # iterating the dataframe and fetching answers
    for index, row in df.iterrows():
        if count == 0:
            break
        if tmpid == row['Id_x'] and subcount > 0:
            s += fetch_answer_for_web(row)
            subcount -= 1
        else:
            if distance(query, row['Title_vector']) < bottleneck:
                tmpid = row['Id_x']
                s += '######## title of question ########<br>'
                s += row['Title'] + "<br>"
                s += fetch_answer_for_web(row)
                count -= 1
                subcount = 3

    if s == "":
        return "No results found"
    else:
        return s
