import requests
from bs4 import BeautifulSoup
import pprint


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'],
                  reverse=True)  # it does not know how to sort dictionaries to we have to sort with
    # lambda


def create_custom_hn(links, subtext):  # hackernews
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].findAll('a')[0].get('href', None)  # the second param is the default: None
        try:
            vote = subtext[idx].select('.score')
            if len(vote):
                points = int(vote[0].getText().replace(' points', ''))
                if points > 99:  # you can customize this to show only high ranking votes
                    hn.append({'title': title, 'link': href, 'votes': points})
        except:
            print("no votes present!!!!!! ")
        # some stories do not have votes

    return sort_stories_by_votes(hn)


# how to get more than one page from hackernews
pages_to_scan = 2  # one is default

current_page = 1

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
# print(res.text)  # this gets us the html file

soup = BeautifulSoup(res.text, 'html.parser')  # this makes it as actual html because it was text format
soup2 = BeautifulSoup(res2.text, 'html.parser')  # this makes it as actual html because it was text format
votes = soup.select('.score')

votes2 = soup2.select('.score')
links = soup.select('.titleline')
subtext = soup.select('.subtext')
links2 = soup2.select('.titleline')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2



pprint.pprint(create_custom_hn(mega_links, mega_subtext))

print(f"___PROGRAM DONE")
