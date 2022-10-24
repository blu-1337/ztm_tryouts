import tweepy
import time

auth = tweepy.OAuth1UserHandler(
    'wx02sMuDQkqUnFBvgRpi4gP80', 'VSs3j2FLOhPfaAKG06CvcLnQJq6T6xirzv8mtdIPGPtH1aoeTB',
    '188697633-irPiBpmnGWYMNQ2fCHkhsgKpdKJ0ZFFr96vL67Vr', '4ZgCnBrcYW8UQig4oDJYhxOu12yPj4e3wcCuWJRIkLJwe'
)  # you get this from your twitter api development profile, cgwiki too

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)  # gets all our tweets




def limit_handler(cursor):  # do not fetch everything at once, avoid flooding
    try:
        while True:
            yield cursor.next()
    except tweepy.TooManyRequests:
        time.sleep(1000)
    except StopIteration:  # this stops the iteration so we just return something
        return


# Generous Bot: this follows back a certain follower if their name is on your followers list
# for follower in limit_handler(tweepy.Cursor(api.get_followers).items()):
#     if follower.name == "Elon Musk":
#         follower.follow()
#         break


# this adds likes to posts that contain that search string
search_string = 'python'
number_of_tweets = 2  # number of tweets to like

for tweet in tweepy.Cursor(api.search_tweets, search_string).items(number_of_tweets):
    try:
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepyException as e:
        print(e)
    except StopIteration:
        break
