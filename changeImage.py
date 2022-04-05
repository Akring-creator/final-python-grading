#shebang
from PIL import Image
import os

PATH = './imagedummy/file'
SRC = PATH
OUTPUT = PATH
pattern = r'^([\w\d_ ]+)\.\w+$'

for file in os.listdir(SRC):
    im = Image.open(os.path.join(SRC, file))
    result = re.search(pattern, file)
    print(result)
    im = im.convert('RGB')
    path = os.path.join(OUTPUT, result[1]+'.jpeg' )
    im.resize((600,400)).save(path)

for img in os.listdir(PATH):
    if ".jpeg" in img:
        print(img)
