import tweepy
import time

consumer_key = '9X0sGt5hWaG6bYUvKOjpYaWnf'
consumer_secret = 'IiqiYHvkacrAAnjjxooqnluRCFtwOwWKIy8ImgwV7Y4gZ6TgJ5'

access_token = '1466043779031486470-KWbmd2DWODwmYI7O3DRFgWK9gRMN6O'
access_token_secret = 'ZuH6vbgxPYd0G99xBhYTIPFdXoBNcKfCMFhkwJ3AJrkln'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
client = tweepy.Client(auth)

# functions:
# likes whenever gabby tweets

FILE_NAME = 'seen_tweet.txt'

def read_seen_tweet(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    seen_tweet_id = int(file_read.read().strip())
    file_read.close()
    return seen_tweet_id

def write_seen_tweet(FILE_NAME, seen_tweet_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(seen_tweet_id))
    file_write.close()
    return

def fav():
    gabby_tweets =  api.user_timeline(since_id = read_seen_tweet(FILE_NAME), user_id = '734574794', tweet_mode = 'extended')
    for tweet in reversed(gabby_tweets):
        if 'rt' not in tweet.full_text.lower():
            print(tweet.user.screen_name + ' - ' + str(tweet.id) + ' - ' + tweet.full_text)
            # api.create_favorite(tweet.id)
            write_seen_tweet(FILE_NAME, tweet.id)

fav()

# while True:
#     fav()
#     time.sleep(60)