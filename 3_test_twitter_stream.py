
from twython import TwythonStreamer
import sys
import json
import time

tweets = []

class MyStreamer(TwythonStreamer):
    '''our own subclass of TwythonStremer'''

    # overriding
    def on_success(self, data):
        #print(data)
        if 'lang' in data and data['lang'] == 'en' and data['retweeted'] == False and data['text'].find(keyword)>-1:
            #print type(data['text'])
            tweets.append(data)
            print 'received tweet #', len(tweets), data['text']
    
#
        if len(tweets) >= 10:
            self.store_json()
            self.disconnect()

    # overriding
    def on_error(self, status_code, data):
        print status_code, data
        self.store_json()
        self.disconnect()

    def store_json(self):
        timestr = time.strftime('%Y%m%d-%H%M%S')
        filename = 'tweet_{}_{}_{}.json'.format(keyword, timestr,len(tweets)) 
        with open( filename, 'w') as f:
            json.dump(tweets, f, indent=4)


if __name__ == '__main__':

    with open('your_twitter_credentials.json', 'r') as f:
    #with open('../../../JG_Ch09_Getting_Data/04_api/gene_twitter_credentials.json', 'r') as f:
        credentials = json.load(f)

    # create your own app to get consumer key and secret
    CONSUMER_KEY = credentials['CONSUMER_KEY']
    CONSUMER_SECRET = credentials['CONSUMER_SECRET']
    ACCESS_TOKEN = credentials['ACCESS_TOKEN']
    ACCESS_TOKEN_SECRET = credentials['ACCESS_TOKEN_SECRET']

    stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    if len(sys.argv) > 1:
        keyword = sys.argv[1]
    else:
        keyword = 'Justin'
    
    stream.statuses.filter(locations='-125.375977,52.199190,-97.998047,68.054836')
    
    
