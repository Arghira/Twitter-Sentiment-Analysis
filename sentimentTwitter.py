import tweepy
from textblob import TextBlob

consumer_key = 'PERSONAL_CONSUMER_KEY'
consumer_secret = 'PERSONAL_CONSUMER_SECRET'

access_token = 'PERSONAL_ACCESS_TOKEN'
access_token_secret = 'PERSONAL_ACCESS_TOKEN_SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('RZA')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
