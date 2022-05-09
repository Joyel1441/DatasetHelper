from bs4 import BeautifulSoup
import urllib3
import wget
import os

class ImageDownloader:
    def __init__(self, keywords, limit=10, output_dir="./images"):  
        self.keywords = keywords
        self.limit = limit
        self.output_dir = output_dir
        if (os.path.exists(self.output_dir) == False):
            os.mkdir(self.output_dir)
        http = urllib3.PoolManager()
        #Download images from unsplash
        url = "https://unsplash.com/s/photos/" + keywords
        response = http.request('GET', url)
        soup = BeautifulSoup(response.data, 'html.parser')
        image_links_temp = []
        self.image_links = []
        for img in soup.findAll('img'):
            image_links_temp.append(img.get('src'))

        for img in image_links_temp:
            if img != None and img.startswith('https://'):
                self.image_links.append(img)

    def download(self):
        for img in self.image_links[:self.limit]:
            wget.download(img, out=self.output_dir)
        print('Download Complete')
         
    
