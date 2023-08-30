from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage,"html.parser")


articles = soup.find_all(name="a", rel="noreferrer")
article_texts = []
article_links = []
for tag in articles:
    text = tag.getText()
    link = tag.get("href")
    if text and link:
        article_texts.append(text)
        article_links.append(link)

article_upvotes = [score.getText() for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvotes)