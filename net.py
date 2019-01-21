import requests
from bs4 import BeautifulSoup
import shutil
import time
import os

def download_file(imgUrl, imgPath):
    response = requests.get(imgUrl, stream=True)
    if response.status_code == 200:
        with open(imgPath, "wb") as f:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, f)


HEADER = {
'User-Agent': "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)",
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'en-US,en;q=0.5',
'Connection': 'keep-alive',
'Accept-Encoding': 'gzip, deflate',
}

url = "https://movie.douban.com/"

# data = ""
# with open("data", encoding="utf-8") as f:
#     data = f.read()

response = requests.get(url, headers=HEADER)
time.sleep(1)

soup = BeautifulSoup(response.text, "lxml")


ddir = os.path.abspath('./down')
imgdir = os.path.abspath('./img')
outFile = os.path.join(ddir, 'out.txt')

with open(outFile, 'a', encoding='utf-8') as of:
    for li in soup.find_all('li', class_='poster'):
        for a in li.find_all('a'):
            filmName = ''
            imgUrl = ''
            link = a.get('href')
            for img in a.find_all('img'):
                filmName = img.get('alt')
                imgUrl = img.get('src')

            # imgSavePath = os.path.join(imgdir, os.path.basename(imgUrl))
            imgSavePath = os.path.join(imgdir, filmName + '.jpg')
            download_file(imgUrl, imgSavePath)
            of.write(filmName + ", " + link + ", " + imgUrl + '\n')



