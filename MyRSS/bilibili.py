from config.config import Config
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup


def get_bilibili_data():
    user_agent = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"
    }
    url = "https://www.bilibili.com"
    request = urllib.request.Request(url, headers=user_agent)
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)


if __name__ == '__main__':
    get_bilibili_data()
