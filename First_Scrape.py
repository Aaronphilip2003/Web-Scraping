import requests
import html5lib
from bs4 import BeautifulSoup

url="https://www.scrapethissite.com/pages/"

r=requests.get(url)

htmlcontent=r.content

soup=BeautifulSoup(htmlcontent,'html.parser')

title=soup.title
# print(title) # soup object
# print(title.string) # navigable string
# print(soup.prettify)

print(title.string)

# get all the paragraphs in the website
paras=soup.find_all('p')

# get a particular class of all the paragraphs
classpara=soup.find_all('p',class_="lead session-desc")

# get the text from the tags
tag_text=soup.find('p').get_text()

# get the soup text
# print(soup.get_text())

# grab all the anchor tags
anchors=soup.find_all('a')

# get all the links on a page ( this will just give you the /xyz things which you cannot click)

# for links in anchors:
#     print(links.get('href'))

# now we'll add the base link as well as the /xyz things

all_links=set()

for links in anchors:
    if (links.get('href')!='#'):
        all_links.add("https://www.scrapethissite.com"+links.get('href'))

for links in all_links:
    print(links)
    
# getting all the paragraphs in the webpage

all_paras=set()

for paragraphs in paras:
    p=soup.find('p')
    all_paras.add(p)
    
print(all_paras)

site_nav=soup.find(id="site-nav")

# for element in site_nav.contents: # .contents gives tags a list
#     print(element)
    
# for element in site_nav.children: # .childen gives tags as generators
#     print(element)

# for item in site_nav.strings:
#     print(item)

# better than .strings is to strip the string

for item in site_nav.stripped_strings:
    print(item) # it removes the unneccessary gaps between the strings


# print the parent tags

print(site_nav.parent)