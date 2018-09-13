import logging
import codecs
import io
import pickle
import os
import sys
from pprint import pprint

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding= 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
new_word_search = pickle.load(codecs.open('new_word_search.p','rb'))
#print(new_word_search)
f= codecs.open('new_word_search.txt','w')
for i in range(len(new_word_search)):
    f.write(str(new_word_search[i]))
    f.write('\n')

f.close()

