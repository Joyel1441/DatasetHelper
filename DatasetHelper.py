import requests
import os
import wget

class BulkImageDownloader:
    def __init__(self, keywords, limit=10, output_dir="./images", api_key="27299598-e3c79d76c20f5052cf7ee7429"):  
        self.keywords = keywords
        self.limit = limit
        self.output_dir = output_dir
        self.api_key = api_key
        if (os.path.exists(self.output_dir) == False):
            os.mkdir(self.output_dir)
        
        self.image_links = []
        temp_response = requests.get(f"https://pixabay.com/api/?key={self.api_key}&q={self.keywords}&image_type=photo")
        temp_json_resp = temp_response.json()
        tot_len = temp_json_resp["totalHits"]
        per_page = tot_len//200
        for i in range(per_page):
            response = requests.get(f"https://pixabay.com/api/?key={self.api_key}&q={self.keywords}&image_type=photo&per_page=200&page={i+1}")
            json_resp = response.json()
            for img in json_resp["hits"]:
                self.image_links.append(img["largeImageURL"])


    def download(self):
        base_name = self.keywords.split(" ")[0]
        for idx, img in enumerate(self.image_links[:self.limit]):
            img_name = base_name+str(idx+1)
            resp = requests.get(img, stream=True)
            with open(os.path.join(self.output_dir,img_name+".jpg"), "wb") as f:
                f.write(resp.content)

         
    
