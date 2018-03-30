import jieba
import logging
import sys
from gensim.corpora import WikiCorpus

import codecs
import csv
import io
import pickle
import os
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

logging.basicConfig(format = '%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

#jieba.set_dictionary('../dict.txt.big')

stopword_set = set()

with codecs.open('../stop_words.txt','r','utf-8') as stopwords:
    for stopword in stopwords:
        stopword_set.add(stopword.strip('\n'))
    
output  = codecs.open("wiki_seg.txt",'w','utf-8')
with codecs.open("./wiki.text",'r','utf-8') as content:
    for texts_num, line in enumerate(content):
        line = line.strip('\n')
        words = jieba.cut(line, cut_all=False, HMM = True)
        for word in words:
            if word not in stopword_set:
                output.write(word + ' ')
        output.write('\n')


        if (texts_num +1 ) % 10000 == 0:
            logging.info("已完成前 %d 行的斷詞" % (texts_num + 1))

output.close()






