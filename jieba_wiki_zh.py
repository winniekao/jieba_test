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
jieba.load_userdict("../../food_proj/eat.dic")
jieba.load_userdict("../../food_proj/eat_zhTW.dic")

stopword_set = set()
all_word_cut = []

with codecs.open('../../food_proj/stop_words.txt','r','utf-8') as stopwords:
    for stopword in stopwords:
        stopword_set.add(stopword.strip('\n'))
    
output  = codecs.open("wiki_seg_zh.txt",'w','utf-8')
with codecs.open("./wiki_2.text",'r','utf-8') as content:
    for texts_num, line in enumerate(content):
        line = line.strip('\n')
        words = jieba.cut(line, cut_all=False, HMM = True)
#        words = jieba.cut_for_search(line, HMM = True)
        sentence = ""
        for word in words:
            if word not in stopword_set:
#                sentence = sentence + word + ' '
                output.write(word + ' ')
#                if word not in all_word_cut:
#                    all_word_cut.append(word)
        output.write('\n')
#            sentence += '\n'
#            all_word_cut.append(sentence)



        if (texts_num +1 ) % 10000 == 0:
            logging.info("已完成前 %d 行的斷詞" % (texts_num + 1))

#pickle.dump(all_word_cut, codecs.open('all_word_cut','w','utf-8'))
#pickle.dump(all_word_cut, codecs.open('wiki_word_cut.p', 'wb'))
output.close()







