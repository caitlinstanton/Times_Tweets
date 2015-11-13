import tweepy
import datetime
import csv

consumer_key="D5xNoFTpMAAsdEpT08ZSs1Wcj"
consumer_secret="xn3nmwcJEU6hfoH7NND8zX2aYbKwD3iEIQjlJFr6ouubWRNrJg"

access_token="925616599-u6yMmcLB3Ar9RZq80e0wUTCZjZp5TotXapkTOxyQ"
access_token_secret="E5DTEg4DGFmFGTKbCusko1tfjPgpWEvWLw68b6MCi64EB"

def search(hashtag):
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)

  api = tweepy.API(auth)
  result = api.search(q=hashtag, rpp = 100)

  with open('tweets.csv', 'wb') as csvfile:
      spamwriter = csv.writer(csvfile)
      spamwriter.writerow(('Time','Tweet'))
      for  tweet in result:
        content = tweet.text.encode('utf-8').strip()
        time    = tweet.created_at
        spamwriter.writerow((time, content))

hashtag = raw_input("what hash do you want to search?")

search(hashtag)
print 'success!'
