import tweepy
import time



# 0 = SquaredMySide, 1 = GabbNicoh
acc = 0

auth = tweepy.OAuthHandler(consumer_key[acc], consumer_secret[acc])
auth.set_access_token(access_token[acc], access_token_secret[acc])

api = tweepy.API(auth)

# functions:
# likes whenever a user tweets
user = [['miles', '1113273285460910082'],
        ['gabb', '734574794']]

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
    tweets =  api.user_timeline(since_id = read_seen_tweet(FILE_NAME), user_id = user[0][1], tweet_mode = 'extended')
    for tweet in reversed(tweets):
        if 'RT' not in tweet.full_text:
            print(tweet.user.screen_name + ' - ' + str(tweet.id) + ' - ' + tweet.full_text)
            api.create_favorite(tweet.id)
            write_seen_tweet(FILE_NAME, tweet.id)

print('Seener 1.1 Initializing...')
while True:
    fav()
    time.sleep(5)

