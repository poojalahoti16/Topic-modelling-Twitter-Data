import  json
import os


def readTweets(file1):
    infile = open(file1, 'r')
    lines = infile.read()
    infile.close()

    jsonList = json.loads(lines)

    global i;
    for each in jsonList:
#        print str(i) + '--' + each
        i += 1



i=0
#fileList = os.listdir('.')
#
#extractTag = '_extracted.json'

read_tweets = 'extracted_Tweets.json'

readTweets(read_tweets)

print i

