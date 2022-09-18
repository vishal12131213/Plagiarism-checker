import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
import string
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
#nltk.download('all')
stopWords=set(stopwords.words('english'))
df=pd.read_csv('D:/project/sample.txt')
p=[doc for doc in os.listdir() if doc.endswith('.csv')]
#print(p)
std=[open(_file,encoding='utf-8').read() for _file in p]
#print(std)
#print(df)
def plag(a):
    
    #print(df)
    
    #print(stopWords)
    #nltk.download('stopwords')
    #print(stopwords.words('english'))
    cleaning=[i for i in a if i not in string.punctuation]
    #print(cleaning)
    cleaning=''.join(cleaning)
    #print(cleaning)
    return(j for j in cleaning.split() if j.lower() not in stopwords.words('english'))
#print(df.shape)
plag(std)
vct=TfidfVectorizer(analyzer=plag).fit_transform(std).toarray()
#gt=bow_transformer.transform(df['text'])
#print(vct)
#x=gt.toarray()
#print(x)
#print(vct.shape)
s_vct=list(zip(p,vct))
#print(s_vct)
def similarity(doc1,doc2):
    return cosine_similarity([doc1,doc2])
plag_res=set()
def check():
    global vct
    for n1,t1 in s_vct:
        cp1=s_vct.copy()
        current_index=cp1.index((n1,t1))
        #print(current_index)
        del cp1[current_index]
        for n2,t2 in cp1:
            sim_score=similarity(t1,t2)[0][1] 
            #print(sim_score)
            n_pair=sorted((n1,n2))
            #print(n_pair)
            score=(sim_score)
            plag_res.add(score)
    #print(score)        
    return plag_res
#for data in check():
    #print(data*100,"%")   
