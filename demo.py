from gensim.models import word2vec
from gensim import models
import logging


import codecs
import csv
import io
import pickle
import os
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'UTF-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'UTF-8')
sys.stdin = io.TextIOWrapper(sys.stdin.detach(), encoding = 'UTF-8')

model = models.Word2Vec.load("./word2vec_wiki_zhTW_search.model")
model_2 = models.Word2Vec.load("./word2vec_wiki_zhTW.model")
while True:
    try:
        query = input(">> ")
#        query = query.encode('utf-8')
        q_list = query.split()
        real_model = model

        if len(q_list) == 1:
            print("相似詞前100排序")
            if q_list[0] not in model:
                real_model = model_2
            res = real_model.similar_by_word(q_list[0], topn = 10)
            for item in res:
                print(item[0]+", "+str(item[1]))

        elif len(q_list) ==2:
            print("計算 Cosine 相似度")
            res = real_model.similarity(q_list[0], q_list[1])
            print(res)

        else:
            print("%s之於%s , 如%s之於" % (q_list[0], q_list[2], q_list[1]))
            res = real_model.most_similar([q_list[0],q_list[1],[q_list[2]]], topn = 10)
            for item in res:
                print(iten[0]+","+str(item[1]))

        print("--------------------------------------------")

    except Exception as e:
        print(repr(e))

