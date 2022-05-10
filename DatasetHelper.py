import requests
import os

class BulkImageDownloader:
    def __init__(self, keywords, limit=10, output_dir="./images", api_key="27299598-e3c79d76c20f5052cf7ee7429"):  
        self.keywords = keywords
        self.limit = limit
        self.output_dir = output_dir
        self.api_key = api_key
        self.image_found = True
        
        self.image_links = []
        temp_response = requests.get(f"https://pixabay.com/api/?key={self.api_key}&q={self.keywords}&image_type=photo")
        temp_json_resp = temp_response.json()
        tot_len = temp_json_resp["total"]
        if (tot_len == 0):
            print('No images found')
            self.image_found = False
            return
        per_page = self.limit//tot_len
        pages = tot_len//per_page
        if (tot_len > self.limit):
            per_page = tot_len//200
            pages = 200
        else:
             print(f"You gave {self.limit} images but only {tot_len} images found")
             choice = input(f"Do you want to download only {tot_len} images? (y to continue, other char to exit) ")
             if (choice.lower() == "y"):
                 pass
             else:
                 self.image_found = False
                 return
        
        for i in range(per_page):
            response = requests.get(f"https://pixabay.com/api/?key={self.api_key}&q={self.keywords}&image_type=photo&per_page={pages}&page={i+1}")
            json_resp = response.json()
            for img in json_resp["hits"]:
                self.image_links.append(img["largeImageURL"])


    def download(self):
        if (self.image_found):
            if (os.path.exists(self.output_dir) == False):
                os.mkdir(self.output_dir)
            print('Download started')
            base_name = self.keywords.split(" ")[0]
            for idx, img in enumerate(self.image_links[:self.limit]):
                img_name = base_name+str(idx+1)
                resp = requests.get(img, stream=True)
                with open(os.path.join(self.output_dir,img_name+".jpg"), "wb") as f:
                    f.write(resp.content)
            print('Download complete')
