import pickle
import codecs
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import numpy as py
from pprint import pprint
from collections import OrderedDict

from gensim.corpora import WikiCorpus
import logging
import codecs
import csv
import sys
import io
import os
import jieba
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

jieba.load_userdict("../../food_proj/eat.dic")
jieba.load_userdict("../../food_proj/eat_zhTW.dic")
stopword_set = set()
wiki_corpus = WikiCorpus('./zhwiki-20180520-pages-articles.xml.bz2', dictionary = {})
text_num = 0

with codecs.open('../../food_proj/stop_words.txt','r','utf-8') as stopwords:
    for stopword in stopwords:
        stopword_set.add(stopword.strip('\n'))
each_doc = []
for text in wiki_corpus.get_texts():
    data = b' '.join(text)
    all_data = str(data, encoding='utf8')+'\n'
    each_doc.append(all_data)
    text_num += 1
#    print(data)
#each 10000 doc into pickle 
    if text_num % 1000 == 0:
        jieba_each_doc = []
# jieba each doc
#        for texts_num , line in enumerate(each_doc):
        for i in range(len(each_doc)):
            line = each_doc[i]
#            print(line)
            line = line.strip('\n')
            words = jieba.cut(line, cut_all=False, HMM = True)
            sentence = ""
            for word in words:
                if word not in stopword_set:
                    sentence = sentence+word+' '
            jieba_each_doc.append(sentence)
# use sklearn tf-idf
        vectorizer = CountVectorizer()
        transformer = TfidfTransformer()
        tfidf =  transformer.fit_transform(vectorizer.fit_transform(jieba_each_doc))
        words = vectorizer.get_feature_names()
        weight = tfidf.toarray()
        file_name_words = './tf_idf_file/'+str(text_num +1)+"_words.p"
        file_name_weight = './tf_idf_file/'+str(text_num +1)+"_weight.p"
        pickle.dump(words, codecs.open(file_name_words, 'wb'))
        pickle.dump(weight, codecs.open(file_name_weight,'wb'))
        jieba_each_doc.clear()
        each_doc.clear()
        logging.info("已完成前 %d 行的tf-idf" % (text_num +1))



