import jieba
import logging
import sys
from gensim.corpora import WikiCorpus
from opencc import OpenCC
import codecs
import csv
import io
import pickle
import os
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

logging.basicConfig(format = '%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
jieba.load_userdict("./eat.dic")
#jieba.set_dictionary('../dict.txt.big')

stopword_set = set()
all_word_search = []
cc = OpenCC('s2tw')

with codecs.open('../stop_words.txt','r','utf-8') as stopwords:
    for stopword in stopwords:
        stopword_set.add(stopword.strip('\n'))
    
output  = codecs.open("wiki_seg_zhtw_search.txt",'w','utf-8')
with codecs.open("./wiki.text",'r','utf-8') as content:
    for texts_num, line in enumerate(content):
        line = line.strip('\n')
        channge_tw_line = cc.convert(line)
#        print(channge_tw_line)
#        words = jieba.cut(line, cut_all=False, HMM = True)
        words = jieba.cut_for_search(channge_tw_line, HMM=False)
        for word in words:
            if word not in stopword_set:
                output.write(word + ' ')
#                if word not in all_word_search:
#                    all_word_search.append(word)
        output.write('\n')


        if (texts_num +1 ) % 10000 == 0:
            logging.info("已完成前 %d 行的斷詞" % (texts_num + 1))

#pickle.dump(all_word_search, codecs.open('all_word_search','w','utf-8'))
output.close()







