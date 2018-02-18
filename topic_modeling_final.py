
# importing os
import os
import re
# importing json
import json

# importing numpy
import numpy as np

# importing nltk
import nltk

# importing count vectorizer and tfidfvectorizer from scikit learn
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# importing decomposition from sklearn
from sklearn import decomposition

# importing gensim corpora
from gensim import corpora

# importing models from gensim
from gensim import models


from nltk.stem.lancaster import LancasterStemmer
ls = LancasterStemmer()


def clean_tweet(tweet):
       
    return (re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", tweet).split())


    
stopwords = nltk.corpus.stopwords.words('english')
stopwords.append(unicode("make", "utf-8"))
stopwords.append(unicode("got", "utf-8"))
stopwords.append(unicode("say", "utf-8"))
stopwords.append(unicode("guess", "utf-8"))
stopwords.append(unicode("look", "utf-8"))

#,'make','guess',"say","got","look"
specialList =['trump','https','donald','nunes',"http","ok","no","like","amp"]
#import nltk
#stopwords = nltk.corpus.stopwords.words('english')

tweets = 'extracted_Tweets.json'

tweet_text_corpus = list()
docs = list()

clean_tweet_text = ''
#path = 'full_tweet/'
filestart = 'tweet_trump'


for filename in os.listdir('.'):
    # print filename
    if filename.startswith(filestart): 
        clean_tweet_text = ''
        with open(filename, 'r') as infile:
            
            inner_doc_list = list()
        
            lines = infile.read()
            infile.close()
            jsonObjects = json.loads(lines)
    
        
            for each in jsonObjects:
                
                try:
                    tweet_text = each['text']
                except:
                    tweet_text = each
                    
                wordlist = clean_tweet(tweet_text)   
                for word in wordlist:
                    # print type(word)
                    if len(word) == 1 or word in stopwords :
                         continue
                
                    if any(s in word.lower() for s in specialList):
                        continue
                    #word = ls.stem(word)
                    inner_doc_list.append(word)
                    clean_tweet_text += ' {}'.format(word.encode('utf-8'))
        docs.append(inner_doc_list)
        tweet_text_corpus.append(clean_tweet_text)

vectorizer = TfidfVectorizer(stop_words='english', min_df=2)
dtm = vectorizer.fit_transform(tweet_text_corpus)

vocab = vectorizer.get_feature_names()

num_topics = 7
clf = decomposition.NMF(n_components=num_topics, random_state=1)
doctopic = clf.fit_transform(dtm)


topic_words = list()
number_of_topic_words = 10

topic_words = []
num_top_words = 5
for topic in clf.components_:
    # print topic.shape, topic[:5]
    word_idx = np.argsort(topic)[::-1][0:num_top_words]  # get indexes with highest weights
    # print 'top indexes', word_idx
    topic_words.append([vocab[i] for i in word_idx])
    # print topic_words[-1]
    # print

# print '__lol__' * 10


for t in range(len(topic_words)):
    print "Topic {}: {}".format(t, ' '.join(topic_words[t][:10]))

dic = corpora.Dictionary(docs)

corpus = [dic.doc2bow(text) for text in docs]
# print(type(corpus), len(corpus))

tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]

NUM_TOPICS = 7
model = models.ldamodel.LdaModel(corpus_tfidf,
                                 num_topics=NUM_TOPICS,
                                 id2word=dic,
                                 update_every=1,
                                 passes=100)

print("LDA model")
topics_found = model.print_topics(15)
counter = 1
for t in topics_found:
    print("Topic #{} {}".format(counter, t))
    counter += 1
