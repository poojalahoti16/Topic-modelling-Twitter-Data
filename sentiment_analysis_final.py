# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 22:11:30 2017

@author: Pooja Lahoti
"""
import re
from textblob import TextBlob
import matplotlib.pyplot as plt
import json
import numpy as np



def clean_tweet(tweet):
       
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", tweet).split())
 
def get_tweet_sentiment(tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(clean_tweet(tweet))
        # set sentiment
#        if analysis.sentiment.polarity > 0:
#            return 'positive'
#        elif analysis.sentiment.polarity == 0:
#            return 'neutral'
#        else:
#            return 'negative'
        return analysis




sub_list = []
pol_list = []
count_pos = 0
count_neg = 0
count_neu = 0

tweets = 'extracted_Tweets.json'

with open(tweets,"r") as infile:
    lines = infile.read()
    infile.close()

    jsonList = json.loads(lines)

    
for tweet in jsonList:
    tb = get_tweet_sentiment(tweet)
    sub_list.append(tb.sentiment.subjectivity)
    pol_list.append(tb.sentiment.polarity)
# To get count of Extreme POSITIVE AND NEGATIVE TWEETS:
#    if tb.sentiment.polarity > 0.5:
#        count_pol += 1
#    else:
#        count_neg += 1
#    if tb.sentiment.polarity > 0.5:
#        count_pos += 1
#    elif tb.sentiment.polarity < -0.5:
#        count_neg += 1
#    else:
#        count_neu += 1
#   To get the count of all the POSITIVE and NEGATIVE TWEETS:

#    if tb.sentiment.polarity > 0:
#        count_pos += 1
#    elif tb.sentiment.polarity < 0:
#        count_neg += 1
#    else:
#        count_neu += 1
#To get count of NEUTRAL TWEETS
    if -0.5 < tb.sentiment.polarity < 0.5:
        count_neu  += 1
    
    
print sub_list
print ("------------------------------------------------------------------")

print pol_list


plt.hist(sub_list) #, normed=1, alpha=0.75)
plt.xlabel('subjectivity score')
plt.ylabel('sentence count')
plt.grid(True)
#plt.savefig('subjectivity.pdf')
plt.axvline((sum(sub_list)/ float(len(sub_list))), color='r', linestyle='dashed', linewidth=1)
plt.show()

plt.hist(pol_list) #, normed=1, alpha=0.75)
plt.xlabel('polarity score')
plt.ylabel('sentence count')
plt.grid(True)
plt.savefig('polarity.pdf')
plt.axvline((sum(pol_list)/ float(len(pol_list))), color='r', linestyle='dashed', linewidth=1)
plt.show()


#ptweets = [tweet for tweet in tweets if tweet["sentiment"] == "positive"]
#print len(ptweets)

print 'Subjectivity Mean:', (sum(sub_list)/ float(len(sub_list)))
print 'Polarity Mean:', (sum(pol_list)/ float(len(pol_list)))
#print count_pos
#print count_neg
print count_neu
