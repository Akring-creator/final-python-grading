import requests
import os

url = 'http://www.example.com'
imgPath = './changeImage/imagedummy/'
imgFiles = os.listdir(imgPath)

for file in imgFiles:
    if '.jpeg' in file:
        with open(imgPath + file, 'rb') as img:
            r = requests.post(url, files={'file': img})
            img.close()
