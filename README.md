# DatasetHelper
Python library for dataset collection and manipulation (will be added) for your next Machine Learning project

## Installation:
##### Step 1:
`git clone https://github.com/Joyel1441/DatasetHelper.git`
##### Step 2:
`cd DatasetHelper`
##### Step 3:
`pip install -r requirements.txt`


## Usage:
### BulkImageDownloader
> BulkImageDownloader helps you download bulk images related to the keywords provided

Load BulkImageDownloader class from DatasetHelper, and then pass keywords (related to image which you want to download) as the argument
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

> More features will be added to ease your work in handling datasets, you can help by contributing this project
