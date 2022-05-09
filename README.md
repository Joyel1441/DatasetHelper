# DatasetHelper
Python library to download bulk images for your next Machine Learning project

(use a VPN if it throws connection error)

## Installation:
##### Step 1:
`git clone https://github.com/Joyel1441/DatasetHelper.git`
##### Step 2:
`pip install -r requirements.txt`

## Usage:
### ImageDownloader
ImageDownloader helps you download bulk images related to the keywords provided
load ImageDownloader class from DatasetHelper, and then pass keyword (image which you want to download) as the argument
```python
from DatasetHelper import ImageDownloader

img = ImageDownloader('plants')
img.download()
```

more features will be added to ease your work in handling datasets, help me in doing so by contributing this project
