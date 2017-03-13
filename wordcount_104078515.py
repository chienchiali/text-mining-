# -*- coding: UTF-8 -*- 
sentences = []
position = 0
for line in open('building_global_community.txt'):
    # 刪減前後的空白(與換行)
    line = line.strip('')
    #print (line)
    
    # 將處理好的字串加入 sentences 
    sentences.append(line)

    #split sentences into words (split)
    sentence = ''.join(sentences)
    
sentence = sentence.replace('-\n','')
sentence = sentence.replace('-',' ')
# print (sentence)
# build stopwords
import nltk
from nltk import word_tokenize
print(word_tokenize(sentence))
from nltk import wordpunct_tokenize
print(wordpunct_tokenize(sentence))

nltk.download('stopwords')
from nltk.corpus import stopwords
stops = set(stopwords.words('english'))
import string
# add more
stops.update(string.ascii_letters + string.punctuation + string.digits)  
#如果我們
stops.update(('--'))
import string
string.punctuation
# you can add one at a time
for symbol in string.punctuation:
    stops.add(symbol)
# or update a sequence into the set
stops.update(string.punctuation)
words = word_tokenize(sentence)
# for word in words:
#     if word not in stopwords:
#         print(word)
print([word for word in words if word not in stops])
words = [word for word in words if word not in stops]
clean = [word for word in words if word.isalpha()]
from collections import Counter
counter = Counter(clean)
counter.most_common(20)

import csv
with open('wordcount.csv', 'w') as csvfile:
    # set up header
    fieldnames = ['word', 'count']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for word, count in counter.most_common():
        writer.writerow({'word': word, 'count': count})
