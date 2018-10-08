import requests
from bs4 import BeautifulSoup

__author__ = "Geoffrey Bachelot"


def nytimes_titles():
    titles = []
    url = 'https://www.nytimes.com/'
    r_html = requests.get(url).text
    soup = BeautifulSoup(r_html, "html.parser")
    r_titles = soup.findAll('h2')
    for title in r_titles:
        titles.append(title.string)
    return '\n'.join(titles)

if __name__ == '__main__':
    print(nytimes_titles())
