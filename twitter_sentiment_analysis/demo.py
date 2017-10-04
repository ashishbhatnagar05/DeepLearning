import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key= 'mvHbyMvJWbEZp2rN7WSU7UHZv'
consumer_secret= 'mRLuQgqx2hkUam783b11lhee7o7NJFsE2dmpDqI2ZiRwASQEOA'

access_token='2468039048-HHurqYQUgUaVJLr89XoR3pvepz3zgtDUmm2ZUmv'
access_token_secret='ivaSeZg93rADA66FQFWxsZrfEIhSB6fzIShaCknA4Jl8D'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('India')



#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment 
#You can decide the sentiment polarity threshold yourself


for tweet in public_tweets:
    print(tweet.text)
    
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")