import requests
import re
from bs4 import BeautifulSoup


def main():
    resp = requests.get('https://www.dcard.tw/f')
    soup = BeautifulSoup(resp.text, 'html.parser')

    posts = soup.find_all('h3')
    for post in posts[:10]:
        print(post.text)



if __name__ == '__main__':
    main()
