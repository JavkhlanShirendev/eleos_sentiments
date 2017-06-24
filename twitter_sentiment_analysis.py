import tweepy
from textblob import textblob

consumer_key = ""
consumer_secret = ""

access_token = ""
access_token_secret = ""

auth = tweepy.OAuthhandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)