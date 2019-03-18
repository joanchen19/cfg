import tweepy

auth = tweepy.OAuthHandler("WmETabftnYCgnUrAr3b9dXJXq","EUcGEy6sKMeVGGARPoC1qoucfRUMXkxNQt2kZRl8Po8YdjrY2n")
auth.set_access_token("1102510442235265026-FKyGkcTBKVFLsanxoLqOgu0hyRsijI", "JA8I8yDSY8dj2zYHSJRJl232eG5LWDKCPQBnYvZytdgGx")

twitter_api = tweepy.API(auth)

cfg_tweets = twitter_api.search(
    q="CodeFirstGirls"
)

for tweet in cfg_tweets:
    print tweet.user.name + ": " + tweet.text + "\n"
