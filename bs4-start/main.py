from bs4 import BeautifulSoup




with open("website.html") as file:
    data = file.read()

soup = BeautifulSoup(data,"html.parser")

print(soup.title.string)
print(soup.prettify())
print(soup.a)
print(soup.li)
print(soup.p)
all_anchor_tags = soup.find_all(name="a")
print (all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))
    heading = soup.find_all( name="h1", id="name")
    
section_heading = soup.find(name="h3", class_="heading")
print(section_heading.get("class"))
headings =soup.select(".heading")
print(headings)
      