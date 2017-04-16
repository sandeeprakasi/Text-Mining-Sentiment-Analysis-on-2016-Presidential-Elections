import datetime
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

consumer_key = 'sbYay36q0Qjh4Aq402pJ1GUbN'
consumer_secret = 'HShlWoDdZ5MZKQNSPDRhJqNivQ8BV7L35Xl4vCMdBnmM1UpQ6x'
access_token = '772752127198367745-yf8F706LrYDlzgkKLJ7abTw03NNDl1B'
access_secret = 'SeAR88pHouGvMNjbTCnqBCO2FltS1YJHZaARkX1dZ3tCp'


fname_prefix = 'Elections_2016'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)


class MyListener(StreamListener):

     def __init__(self):
         self.tweets = []


     def on_data(self, data):
         try:
             self.tweets.append(data);

             print len(self.tweets)

             if len(self.tweets) > 20000:
                 fname = fname_prefix + '-' + ".json"
                 with open(fname, 'a') as f:
                     for tweet in self.tweets:

                         f.write("%s" % tweet)

                 self.tweets = []


             #with open('python.json', 'a') as f:
             #    f.write(data)
             return True
         except BaseException as e:
             print("Error on_data: %s" % str(e))
         return True

     def on_error(self, status):
         print(status)
         return True

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=[''])