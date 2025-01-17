from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')
articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []

for article in articles:
    link = article.get("href")
    article_links.append(link)
    text =  article.get_text()
    article_texts.append(text)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
most_upvotes = article_upvotes.index(max(article_upvotes))
print(article_texts[most_upvotes])
print(article_links[most_upvotes])
