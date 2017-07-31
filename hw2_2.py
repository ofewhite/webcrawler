import requests
import re
from bs4 import BeautifulSoup


def main():
    resp = requests.get('http://blog.castman.net/web-crawler-tutorial/ch2/blog/blog.html')
    soup = BeautifulSoup(resp.text, 'html.parser')


    imgs = soup.find_all('img', {'src': re.compile('crawler.*\.png$')},class_='img img-raised')
    print('總共有幾張圖片含有crawler字串:', len(imgs))

    for imgs in soup.find_all('img', {'src': re.compile('crawler.*\.png$')},class_='img img-raised'):
        print(imgs['src'])
        
if __name__ == '__main__':
    main()