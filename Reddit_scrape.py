from os import link
import requests
from bs4 import BeautifulSoup
import html5lib 

url='https://www.reddit.com/search/?q=programming&t=week'
r=requests.get(url)
htmlcontent=r.content

soup=BeautifulSoup(htmlcontent,'html.parser')

anchors=soup.find_all('a')
all_links=set()

for links in anchors:
    if (links.get('href').startswith('https://www.reddit.com')==True) and (links.get('href').endswith('premium')!=True):
        all_links.add(links.get('href'))

for number,i in enumerate(all_links):
    print(str(number+1)+')',i)