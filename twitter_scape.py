import os
import pandas as pd
import snscrape.modules.twitter as sntwitter
import datetime
import os

def get_tweets(curr_date, prev_date):

    query = '"layoffs" (#techlayoffs OR #layoffs OR #layoff) lang:en until:{} since:{}-filter:replies'
    query_f = query.format(curr_date, prev_date)
    tweets = []
    limit = 1000000
    
    print(query_f)

    i = 1
    for tweet in sntwitter.TwitterSearchScraper(query_f).get_items():
        if len(tweets) == limit:
            break
        else:
            tweets.append([tweet.date, tweet.username, tweet.content, tweet.likeCount, tweet.replyCount, tweet.retweetCount, tweet.retweetedTweet, tweet.user.location])
            
        i += 1

    df1 = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet', 'likeCount', 'replyCount', 'retweetCount', 'retweetedTweet', 'location'])
    print(df1.shape)
    return df1

curr_date = datetime.datetime.today().date().__str__()
prev_date = datetime.datetime.today() - datetime.timedelta(days=1)
prev_date = prev_date.date().__str__()

df_tweets = get_tweets(curr_date, prev_date)

filename = "twitter_{}_to_{}.json".format(prev_date, curr_date)

df_tweets.to_json(filename)
