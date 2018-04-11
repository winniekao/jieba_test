from opencc import OpenCC
import logging
import codecs
import csv
import io
import pickle
import os
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

logging.basicConfig(format = '%(asctime)s : %(levelname)s : %(message)s', level = logging.INFO)

openCC = OpenCC('s2t')
output = codecs.open("wiki_2_zhTW.txt",'w','utf-8')



with codecs.open("./wiki.text",'r','utf-8') as f:
    for  text_num, line in enumerate(f):
        line = line.strip('\n')
        change_text = openCC.convert(line)
        output.write(change_text)

        output.write('\n')

        if (text_num+1 )%10000 ==0:
            logging.info("以完成 %d 行的斷詞" % (text_num+1))

output.close()


