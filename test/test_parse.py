from urllib.request import urlopen
from bs4 import BeautifulSoup


def run():
    url = 'http://www.baidu.com/'
    html = urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    nameList = soup.find_all('span', {'class': 'title-content-title'})

    print('----- name -----')
    for name in nameList:
        print(name.text)
    print('----- child -----')
    for child in soup.find('div', {'id': 's-hotsearch-wrapper'}).children:
        print(child.text)
    # print('----- descendent -----')
    # for descendant in soup.find('div', {'id': 's-hotsearch-wrapper'}).descendants:
    #     print(descendant.text)


if __name__ == '__main__':
    run()
