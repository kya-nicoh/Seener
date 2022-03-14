def followerCount():
    user = api.get_user(screen_name = 'gilliangabb')
    print(user.screen_name)
    print(user.followers_count)

def tweetList():
    tweets =  client.search_all_tweets()
    for tweet in reversed(tweets):
        if 'RT' not in tweet.full_text:
            print(tweet.user.screen_name + ' - ' + str(tweet.id) + ' - ' + tweet.full_text)