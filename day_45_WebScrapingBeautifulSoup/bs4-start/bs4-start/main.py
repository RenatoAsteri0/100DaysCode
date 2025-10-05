import requests
from bs4 import BeautifulSoup

response = requests.get(url='https://news.ycombinator.com/news')
web_page = response.text

soup = BeautifulSoup(web_page, 'html.parser')
articles = soup.find_all(class_='titleline')
articles_text = []
articles_links = []
for article in articles:
    text =  article.getText()
    link = article.find('a').get('href')
    articles_text.append(text)
    articles_links.append(link)

article_upvote = [int(score.getText().strip(' points')) for score in soup.find_all(class_="score")]

print(articles_links)
print(articles_text)
max_value = max(article_upvote)
max_index = article_upvote.index(max_value)

print(f'a historia com mais votos é {articles_text[max_index]} e o link {articles_links[max_index]}')

