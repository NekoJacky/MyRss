from urllib.error import HTTPError, URLError
from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_title():
    url = 'https://www.baidu.com/'
    # 确认需要的环境
    try:
        html = urlopen(url)
    except HTTPError as e:
        print('Error: test_env.py.get_title()')
        print('       html = urlopen(url)')
        print('       HTTPError')
        print(e)
        return None
    except URLError as e:
        print('Error: test_env.py.get_title()')
        print('       html = urlopen(url)')
        print('       URLError')
        print(e)
        return None
    try:
        # print(html.read())
        # print('----- html -----')

        # 确认 python 自带的 html.parser 和两个第三方解析器 lxml 和 html5lib 都可用
        # bs = BeautifulSoup(html, 'lxml')
        # bs = BeautifulSoup(html, 'html5lib')
        bs = BeautifulSoup(html, 'html.parser')
        h = bs.html
    except AttributeError as e:
        return None
    return h


if __name__ == '__main__':
    html = get_title()
    if html is not None:
        print(html)
