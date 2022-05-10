# DatasetHelper
Python library to download bulk images for your next Machine Learning project

## Installation:
##### Step 1:
`git clone https://github.com/Joyel1441/DatasetHelper.git`
##### Step 2:
`pip install -r requirements.txt`

## Usage:
### BulkImageDownloader
> BulkImageDownloader helps you download bulk images related to the keywords provided

Load ImageDownloader class from DatasetHelper, and then pass keyword (image which you want to download) as the argument
```python
from DatasetHelper import BulkImageDownloader

img = BulkImageDownloader('plants')
img.download()
```
> This project uses pixabay api, you can change api key by passing api key as the argument
```python
img = BulkImageDownloader('plants', api_key=<YOUR_PIXABAY_API_KEY>)
img.download()
```
> To change the output directory, you can pass directory name as the argument
```python
img = BulkImageDownloader('plants', output_dir=<OUTPUT_DIRECTORY>)
img.download()
```

> To set the image download limit, you can pass limit as argument
```python
img = BulkImageDownloader('plants', limit=200)
img.download()
```

> More features will be added to ease your work in handling datasets, help me in doing so by contributing this project
