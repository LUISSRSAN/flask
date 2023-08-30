from bs4 import BeautifulSoup




with open("website.html") as file:
    data = file.read()

soup = BeautifulSoup(data,"html.parser")

print(soup.title.string)
print(soup.prettify())
print(soup.a)
print(soup.li)
print(soup.p)
