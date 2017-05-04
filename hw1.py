import requests
from bs4 import BeautifulSoup


def main():
    url='http://blog.castman.net/web-crawler-tutorial/ch1/connect.html'
    title = get_head_text(url, 'title')
    print(title)
    h1 = get_head_text(url, 'h1')
    print(h1)
    p= get_head_text(url, 'p')
    print(p)


def get_head_text(url, head_tag):
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, 'html.parser')
            return soup.find(head_tag).text
    except Exception as e:
        return None


if __name__ == '__main__':
    main()