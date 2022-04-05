import requests
import json
import os
import re

pattern = r'(\d+).\w+'
number_pattern = r'^(\d+) '
descPath = './description/'
imgPath = './changeImage/imagedummy'
desc = os.listdir(descPath)
keys = ['name', 'weight', 'description', 'image_name']
for file in desc:
    tempdict = {}
    with open(descPath + file, 'r') as f:
        read = f.readlines()
        count = 0
        for line in read:
            line = line.strip('\n')
            if keys[count] == 'weight':
                tempdict[keys[count]] = int(re.search(number_pattern, line)[1])
            else:
                tempdict[keys[count]] = line
            count += 1
        f.close()
    tempdict[keys[3]] = re.search(pattern, file)[1] +'.jpeg'
    # jsonformat = json.dumps(tempdict)
    response = requests.post('http://www.example.com/', json = tempdict)
    # print(response.request.body)
