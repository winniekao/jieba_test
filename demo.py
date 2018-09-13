from gensim.models import word2vec
from gensim import models
import logging
from collections import OrderedDict

import codecs
import csv
import io
import pickle
import os
import sys
import pandas as pd
from pprint import pprint
from operator import itemgetter
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'UTF-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'UTF-8')
sys.stdin = io.TextIOWrapper(sys.stdin.detach(), encoding = 'UTF-8')

model = models.Word2Vec.load("./w2v_wiki_food_hmm.model")
model_2 = models.Word2Vec.load("./w2v_wiki_food_search.model")

def most_similar(w2v_model, words,topn=10):
    similar_df = pd.DataFrame()
    for word in words:
        try:
            similar_words = pd.DataFrame(w2v_model.similar_by_word(word, topn=topn), columns=[word,'cos'])
            similar_df = pd.concat([similar_df, similar_words],axis=1)
        except Exception as e:
            print(repr(e))
    return similar_df
def combine_all_similar(words, topen=10) :
    all_dic ={}
    for word in words:
        if word not in model:
            real_model = model_2
        else:
            real_model = model
        try:
            res = real_model.similar_by_word(word, topn=10)
            for item in res:
                if item[0] not in all_dic:
                    all_dic[item[0]] = item[1]
                else:
                    all_dic[item[0]] += item[1]
        except Exception as e:
            print(repr(e))
#    sorted_all_dic = OrderedDict(sorted(all_dic.items(),key = itemgetter(1), reverse = True))
    sorted_all_dic = [[k, all_dic[k]] for k in sorted(all_dic, key=all_dic.get, reverse = True)]
    return(sorted_all_dic)

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
#            print("%s之於%s , 如%s之於" % (q_list[0], q_list[2], q_list[1]))
 #           res = real_model.most_similar([q_list[0],q_list[1],[q_list[2]]], topn = 10)
#            for item in res:
            res = combine_all_similar(q_list)
            pprint(res)

        print("--------------------------------------------")

    except Exception as e:
        print(repr(e))

