from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
article_texts = []
article_links = []
article_tag = soup.find_all(name="span", class_="titleline")
for tag in article_tag:
    article_texts.append(tag.find("a").getText())
    article_links.append(tag.find("a").get("href"))
article_scores = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_links)
print(article_texts)
print(article_scores)

highest_score_index = article_scores.index(max(article_scores))
print(article_texts[highest_score_index])
print(article_links[highest_score_index])