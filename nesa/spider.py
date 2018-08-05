import re
import requests
from bs4 import BeautifulSoup

response = requests.get('http://nesa.zju.edu.cn/index.html')
soup = BeautifulSoup(response.text)

imgtag_list = soup.select('img')
img_list = []
f = open('data.txt', 'a+')

for img in imgtag_list:
    src = img.get('src')
    src = 'http://nesa.zju.edu.cn/index.html/' + src
    print(src)
    f.write(src + '\n')
    f.flush()
    img_list.append(src)

f.close()
