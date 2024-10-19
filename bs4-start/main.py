from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
tag = soup.findAll(name="a", class_ = "storylink")

art_text = []
art_link = []

for item in tag:
    text = item.getText()
    art_text.append(text)

    link = item.get("href")
    art_link.append(link)

a_upvote = [int(score.getText().split()[0]) for score in soup.findAll(name="span", class_="score")]

largest_no = max(a_upvote)
l_index = a_upvote.index(largest_no)

print(art_text[l_index])
print(art_link[l_index])
print(largest_no)


# print(art_text)
# print(art_link)
# print(a_upvote)
