#include packages in need
#for nltk stopwords, the corpus need to be downloaded first
import sqlite3
import nltk
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
import os
import numpy as np
import pandas as pd

os.chdir(r"D://stackoverflow")
stop_words = set(stopwords.words('english'))
df = pd.read_csv('QA.csv',encoding='iso-8859-1')

#return a list of strings representing searching keywords
def clean(query):
    rt=query.split(" ")
    rt=[x for x in rt if x not in stop_words]
    if(rt==[]):return query.split(" ")
    return rt

print("Welcome! ")
query=input("Enter the query: ")
while(len(query)==0):query=input("Enter the query: ") #in case the user inputs empty string
query=clean(query)

#pd.merge(caller,other, on='key', how='left')
#df = pandas.read_csv('Questions.csv',encoding='iso-8859-1')
#conn = sqlite3.connect('Questions.db')
#df.to_sql("Questions.db", conn,index=False,if_exists='append')

#df = pd.read_csv('Questions.csv',encoding='iso-8859-1')
#df1 = pd.read_csv('Answers.csv',encoding='iso-8859-1')
#r=pd.merge(df1,df, left_on='ParentId', right_on='Id',how='left')
#result = r.sort_values(['Score_y', 'Score_x'], ascending=[False, False])

'''
rawexe=
select top(9) p.id as [Post Link], p2.score, p2.body from posts as p
join posts as p2 on p2.parentid = p.id
where p2.id in (
    select top(3) id
    from posts
    where posttypeid = 2 and parentid = p.id
    order by score desc
  )
  and p.title like '%test%a%function%'
  and p.answercount > 10
  and p.tags like '%python%'
  order by p.id asc, p2.score desc;
exe=rawexe.format(clean(query))
'''
#return if all the items in list query are covered in the string tit
def covered(query,tit):
    for q in query:
        if q not in tit:return False
    return True

while(True):
    result=""
    #number of results to render
    count=3
    
    #database column mark: x is for answer and y for question
    for index, row in df.iterrows():
        tit=row['Title']
        
        if(covered(query,tit)):
            count-=1
            result+=row['Title']
            result+='\n'
            result+='\n'
            #parse the html string with beautifulsoup
            #to find all the contents within the tag code
            soup=BeautifulSoup(row['Body_x'],"html.parser")
            tags = soup.find_all('code')
            for i in tags:
                result+=i.text
            result+='\n'
            
            print(result)
            if(count==0):break
    if(result==""):print("No results found. ")
    
    query=input("Type N to quit, else continue. ")
    while(len(query)==0):query=input("Type N/n to quit, else continue. ")
    if(query[0].lower()=='n'):
        break
    else:
        query=input("Enter the query: ")
        while(len(query)==0):query=input("Enter the query: ")
        query=clean(query)

print("See you! ")

