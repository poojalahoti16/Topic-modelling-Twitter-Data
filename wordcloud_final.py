# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 14:12:34 2017

@author: Pooja Lahoti
"""

import nltk
import re
import json
from nltk.stem.wordnet import WordNetLemmatizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt

from nltk.stem.lancaster import LancasterStemmer
ls = LancasterStemmer()
wnl = WordNetLemmatizer()
#reload(sys)  
#sys.setdefaultencoding('utf8')
#from nltk.stem.porter import PorterStemmer
#ps = PorterStemmer()
#
#from nltk.stem.snowball import SnowballStemmer
#ss = SnowballStemmer("english") 
# 
#stopwords.append(unicode("trump", "utf-8"))
#stopwords.append(unicode("https", "utf-8"))
#stopwords.append(unicode("Donald", "utf-8"))
#stopwords.append(unicode("@realdonald", "utf-8"))
#stopwords.append(unicode("RT", "utf-8"))
#stopwords = set(stopwords)
#stopwords.update(("https","geo","trump"))

#print stopwords



def clean_tweet(tweet):
       
    return (re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", tweet).split())


    
stopwords = nltk.corpus.stopwords.words('english')
stopwords.append(unicode("make", "utf-8"))
stopwords.append(unicode("got", "utf-8"))
stopwords.append(unicode("say", "utf-8"))
stopwords.append(unicode("guess", "utf-8"))
stopwords.append(unicode("look", "utf-8"))

#,'make','guess',"say","got","look"
specialList =['trump','https','donald',"http","amp","must","said"]
#import nltk
#stopwords = nltk.corpus.stopwords.words('english')

tweets = 'extracted_Tweets.json'
wordcloudlist = ''


with open(tweets,"r") as infile:
    lines = infile.read()
    infile.close()

    jsonList = json.loads(lines)

    
for tweet in jsonList:    
    wordlist = clean_tweet(tweet)
    #print type(tweet)

    for word in wordlist:
        if len(word) == 1 or word in stopwords :
            continue
        
        if any(s in word.lower() for s in specialList):
           continue
        
        wordcloudlist += ' {}'.format(ls.stem(word))
#print text2    
#out = text2.translate(string.maketrans("",""), string.punctuation)

#ls.stem(out)
#wnl.lemmatize(out)
#ss.stem(out)
#print out

# Generate a word cloud image
#wordcloud = WordCloud().generate(text)


# lower max_font_size
wordcloud1 = WordCloud(max_font_size=40).generate(wordcloudlist) 

# Display the generated image:
plt.figure()
plt.imshow(wordcloud1)
plt.axis("off")
plt.show()

