import requests
from bs4 import BeautifulSoup

def main():
    resp = requests.get('http://blog.castman.net/web-crawler-tutorial/ch2/blog/blog.html')
    soup = BeautifulSoup(resp.text, 'html.parser')



    divs= soup.find_all('div','content')
    for div in divs:
        print([s for s in div.stripped_strings])
    print('總共有幾篇文章:', len(divs))





if __name__ == '__main__':
    main()