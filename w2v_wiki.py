import logging
from gensim.models import word2vec

import codecs
import csv
import io
import pickle
import os
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#logging.basicConfig(format='%(asctime)s : %(levelmame)s : %(message)s', level=logging.INFO )

sentences = word2vec.LineSentence("./wiki_seg.txt")
model = word2vec.Word2Vec(sentences, size=250)

model.save("word2vec_wiki.model")


