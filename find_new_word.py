import logging
import codecs
import io
import pickle
import os
import sys
from pprint import pprint

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding= 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


logging.basicConfig(format = '%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
new_word = []
line_num = 0
with codecs.open('./wiki_seg_zhtw_search_hmm.txt','r','utf-8') as jwh , codecs.open('./wiki_seg_zhtw_search.txt', 'r', 'utf-8') as jw:
    for x, y in zip(jwh, jw):
        line_num+=1
        x = x.strip()
        x_list = x.split(' ')
        y = y.strip()
        y_list = y.split(' ')
#        print('x')
#        print(x_list)
#        print('y')
#        print(y_list)
        hmm_new_word = list(set(x_list)-set(y_list))
#        print('hmm_new')
#        print(hmm_new_word)
        
        for i in range(len(hmm_new_word)):
            if hmm_new_word[i] not in new_word:
                new_word.append(hmm_new_word[i])
#        print('new_word')
#        print(new_word)
        if (line_num)% 100 ==0:
 #           print(line_num)
            logging.info("已完成前 %d 行的比較" % (line_num))
print(new_word)
pickle.dump(new_word, codecs.open('new_word_search.p','wb'))
jwh.close()
jw.close()

