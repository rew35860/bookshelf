import os
import requests
from pathlib import Path
from bs4 import BeautifulSoup


class Book:
    def __init__(self, bookName, startCh, endCh):
        self.bookName = bookName
        self.chapters = range(startCh, endCh+1)
        self.home = str(Path.home())

    # creating a direcotry to store books --> the folder will appear on desktop 
    def createDirectory(self): 
        path = f'{self.home}/Desktop'

        if 'Book' not in os.listdir(path): 
            os.mkdir(f'{path}/Book')
        
        path = f'{path}/Book'
        
        if self.bookName.upper() not in os.listdir(path):
            os.mkdir(f'{path}/{self.bookName.upper()}')


    # parsing html pages and write it on a file 
    def createBook(self):
        try:
            self.createDirectory()

            for number in self.chapters:
                print(f'Currently Scraping Chapter: {number}\n')

                title = '-'.join(self.bookName.lower().split())
                html = requests.get(f"https://readwebnovels.net/novel/{title}/chapter-{number}/")
                soup = BeautifulSoup(html.text, 'html.parser')
                text = soup.findAll('div', {'class':'text-left'})
        
                file1 = open(f'{self.home}/Desktop/Book/{self.bookName.upper()}/chapter_{number}.txt', 'w')
                first = True

                for line in text:
                    l = line.find_all(['p', 'h4'])
                    for i in l: 
                        s = f'{i.text}\n\n'
                        if first: 
                            file1.write('-'*100+'\n\n')
                            first = False

                        file1.write(s)
        except: 
            print('Invalid Title\n')


if __name__ == "__main__":
    read = Book("The Beginning After The End", 1, 2)
    read.createBook()