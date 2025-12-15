from bs4 import BeautifulSoup
import lxml

with open("website.html") as f:
    contents = f.read()

soup = BeautifulSoup(contents, "html.parser") # or "lxml"

print(soup.title) #title.name # title.string

# print(soup.prettify())

print(soup.a) # prints first "a" tag - link (we may search and print <p>)

# if we want all elements - all <p>, we use = soup.find_all(name="a") in list format

all_anchor_tags = soup.find_all(name="a")

for tag in all_anchor_tags:
    # print(tag.getText())
    print(tag.get("href")) # when we need to print particular parameter

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_= "heading")

company_url = soup.select_one(selector="p a ").get("href")
# searches for the first element that matches the CSS selector specified as an argument
print(company_url)

name = soup.select_one("#name")
print(name)

heading = soup.select(".heading")
# searches for all elements with ".heading"
print(heading)