import tweepy
from textblob import TextBlob
from keys import consumer_key, consumer_secret, access_token, access_token_secret
from constants import snp_500
from sentiment_item import SentimentItem
from report import Sentiments
import static
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--d", "-debug")
args = parser.parse_args()

if args.d:
  static.debug_mode = True


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

all_tweet_texts = []
s = Sentiments() 

for snp_ticker in snp_500:
  public_tweets = api.search("#" + snp_ticker, count=20)

  for tweet in public_tweets:
    # print(tweet.text)
    # print ("urls: ", tweet.entities['urls'])
    analysis = TextBlob(tweet.text)
    if (analysis.polarity == 0 and analysis.subjectivity == 0):
      if static.debug_mode:
        print ("continue: polarity and subjectivity = 0")    
        print (tweet.text)
      continue
    if tweet.retweeted:
      if static.debug_mode:
        print ("continue: retweeted: ", tweet.retweeted)
        print (tweet.text)
      continue
    if tweet.source in ("Twitter for iPhone", "Twitter for Android"):
      if static.debug_mode:
        print ("continue: source in iphone or android")
        print (tweet.text)
      continue
    if tweet.text in all_tweet_texts:
      if static.debug_mode:
        print ("continue: text was duplicate")
        print (tweet.text)
      continue

    s_item = SentimentItem(tweet.text, snp_ticker, subjectivity=analysis.subjectivity, polarity=analysis.polarity, multiplier=tweet.retweet_count)
    all_tweet_texts.append(tweet.text)
    s.append(s_item)
    # print (s_item)
    # print ("source: %s, id_str: %s" % (tweet.source, tweet.id_str))

  # print(TextBlob("I didn't like him. His coffee was awful. I dont want to see him again").sentiment)
s.report()