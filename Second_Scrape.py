import requests
import html5lib
from bs4 import BeautifulSoup

url="https://www.crummy.com/software/BeautifulSoup/bs4/doc/"

r=requests.get(url)

htmlcontent=r.content

soup=BeautifulSoup(htmlcontent,'html.parser')

# print(soup.prettify)

all_links=set()
# anchors=soup.find_all('a')


# for links in anchors:
#     if(links.get('href').startswith('h')==True):
#         all_links.add(links.get('href'))

# for item in all_links:
#     print(item)

print(soup.title.string)

paragraphs=soup.find_all('p')

print(soup.get_text())
