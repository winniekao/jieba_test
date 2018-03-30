import logging
import sys
from gensim.corpora import WikiCorpus

import codecs
import csv
import sys
import io
import pickle
import os
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
wiki_corpus = WikiCorpus('./zhwiki-20180301-pages-articles.xml.bz2', dictionary = {})
text_num = 0
with codecs.open("./wiki_2.text",'w',  encoding ='utf-8') as output:
    for text in wiki_corpus.get_texts():
#        print(text)
        data = b' '.join(text)
        output.write(str(data, encoding= 'utf8')+'\n')
    #    output.write(' '.join(text)+'\n')
        text_num += 1
        if text_num %1000 ==0:
            logging.info("已處理 %d 篇文章" % text_num)
