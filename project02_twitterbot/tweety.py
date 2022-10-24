import tweepy
import time

auth = tweepy.OAuth1UserHandler(
    'O7BgAl4ouoIOcncOj5n4bfr1F', 'iAScv87b1LVSQy1iln2UE9L3sJztUTscmlryuDLy8GlF9zDOpA',
    '188697633-BROurss1QQFNcKo8sANipnvTnSCSc9xIGwelSpwG', 'x0XwJcdBUMbom7G5Swp1SCaqNQX4QKR5e9kRMixHamBFx'
)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)  # gets all our tweets

user = api.get_user
print(user)


def limit_handler(cursor):  # do not fetch everything at once, avoid flooding
    try:
        while True:
            yield cursor.next()
    except tweepy.TooManyRequests:
        time.sleep(1000)
    except StopIteration:  # this stops the iteration so we just return something
        return


# # Generous Bot
# for follower in limit_handler(tweepy.Cursor(api.get_followers).items()):
#     if follower.name == "ElonMusk":
#         follower.follow()
#         break

search_string = 'python'
number_of_tweets = 2

for tweet in tweepy.Cursor(api.search_tweets, search_string).items(number_of_tweets):
    try:
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepyException as e:
        print(e.reason)
    except StopIteration:
        break


