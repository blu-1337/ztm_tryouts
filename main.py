import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
# print(res.text)  # this gets us the html file

soup = BeautifulSoup(res.text, 'html.parser')  # this makes it as actual html because it was text format
print(soup)
print(soup.body.contents)
print(soup.body)
print(soup.find_all('div'))
print(soup.find(id='score_33318687'))
print(soup.select('a'))  # CSS selectors
print(soup.select('.score'))
print(soup.select('.storylink')[0])
link = soup.select('.storylink')[0]  # gets first element

votes = soup.select('.score')
print(votes[0].get('id'))



