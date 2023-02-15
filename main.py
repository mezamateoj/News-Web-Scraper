import requests
from bs4 import BeautifulSoup
import typer
import re

r =  requests.get('https://www.reuters.com/article/us-health-coronavirus-global-deaths/global-coronavirus-deaths-pass-agonizing-milestone-of-1-million-idUSKBN26K08Y')
soup = BeautifulSoup(r.text, 'html.parser')

# find the title and author.
article_title = soup.find('h1', class_='Headline-headline-2FXIq').text
article_author = soup.find('a', class_='TextLabel__text-label___3oCVw TextLabel__black-to-orange___23uc0 TextLabel__serif___3lOpX Byline-author-2BSir').text

# Find the p tags that contain the content.
article_content_full = soup.findAll('p',attrs={"class":"Paragraph-paragraph-2Bgue"})

# loop through every p tag and extract the text
article_content = []
for i in article_content_full:
    article_content.append(i.text + '\n')

# join the list with the content previously extracted.    
content = ''.join(article_content)
content = re.sub("[\(\[].*?[\)\]]", "", content)  # remove text inside ()

# still need to implement more functions and add a txt file with all
# info extracted in the scrape.

# add the page content to a txt file
name_file = input('Name the txt file: ')
article_file = open(f'{name_file}.txt', 'w')
article_file.writelines(content)
article_file.close()
#print(article_content)



