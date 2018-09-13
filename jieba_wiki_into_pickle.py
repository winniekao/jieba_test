import logging

import codecs
import pickle
import io
import os
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stedrr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

all_sentence_wiki = []

with codecs.open("./wiki_seg_zh.txt",'r','utf-8') as content:
    for text_num, line in enumerate(content):
        all_sentence_wiki.append(line)

        if (text_num +1) % 10000 ==0:
            logging.info("已完成前 %d 行" % (text_num +1))


pickle.dump(all_sentence_wiki, codecs.open('all_doc_wiki.p', 'wb'))
