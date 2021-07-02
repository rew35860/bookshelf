import os
import requests
from pathlib import Path
from bs4 import BeautifulSoup


class Book:
    def __init__(self, bookName, startCh, endCh):
        self.bookName = bookName
        self.chapters = range(startCh, endCh)
        self.homedir = str(Path.home())

    # creating a direcotry to store books --> the folder will appear on desktop 
    def createDirectory(self): 
        path = f'{home}/Desktop'

        if 'Book' not in os.listdir(path): 
            os.mkdir(f'{path}/Book')
        else: 
            path = f'{path}/Book'
            
            if self.bookName.upper() not in os.listdir(path)
                os.mkdir(f'{path}/{self.bookName.upper()}')
    
    # parsing html pages and write it on a file 
    def createBook(self):
        try:
            self.createDirectory()

            for number in self.chapters:
                print(f'Currently Scraping Chapter: {number}\n')

                title = '-'.join(self.title.lower().split())
                html = requests.get(f"https://readwebnovels.net/novel/{title}/chapter-{number}/")
                soup = BeautifulSoup(html.text, 'html.parser')
                text = soup.findAll('div', {'class':'text-left'})

                file1 = open(f'{home}/Desktop/chapter_{number}.txt', 'w')
                first = True

                for line in text:
                    l = line.find_all(['p', 'h4'])
                    for i in l: 
                        s = f'{i.text}\n\n'
                        if first: 
                            file1.write('-'*200+'\n\n')
                            first = False

                        file1.write(s)
        except: 
            return 'Invalid Title\n'


if __name__ == "__main__":