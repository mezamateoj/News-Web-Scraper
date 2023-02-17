import requests
from bs4 import BeautifulSoup
import re

# still need to implement more functions and add a txt file with all
# info extracted in the scrape.
# maybe add nlp summary of the article, create class and improved all.
# add try except for errors

#print(article_content)
class Article:

    def __init__(self):
        self.url = input('Please Provide the article URL: ')
        self.get_url()
        self.find_content()
        self.extract_text()
        self.export()
        

    def get_url(self):
        r =  requests.get(self.url)
        self.soup = BeautifulSoup(r.text, 'html.parser')

    def find_content(self):
        # find the title and author.
        self.title = self.soup.find('h1', class_='Headline-headline-2FXIq').text
        self.author = self.soup.find('a', class_='TextLabel__text-label___3oCVw TextLabel__black-to-orange___23uc0 TextLabel__serif___3lOpX Byline-author-2BSir').text

        # Find the p tags that contain the content.
        self.content_full = self.soup.findAll('p',attrs={"class":"Paragraph-paragraph-2Bgue"})


    def extract_text(self):
        # loop through every p tag and extract the text
        article_content = []
        for i in self.content_full:
            article_content.append(i.text + '\n')

        # join the list with the content previously extracted.    
        self.content = ''.join(article_content)
        self.content = re.sub("[\(\[].*?[\)\]]", "", self.content)  # remove text inside ()
        return self.content

    def export(self):
        # add the page content to a txt file
        name_file = input('Name the txt file: ')
        self.article_file = open(f'{name_file}.txt', 'w')
        self.article_file.write(f'{self.title}\n')
        self.article_file.write('\n')
        self.article_file.write(f'Author {self.author}\n')
        self.article_file.write('\n')
        self.article_file.writelines(self.content)
        self.article_file.close()

new_Article = Article()


        




