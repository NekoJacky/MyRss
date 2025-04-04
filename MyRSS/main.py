from config.config import Config


class MyRSS:
    def __init__(self):
        self.config = Config()

    def run(self):
        pass


if __name__ == '__main__':
    rss = MyRSS()
    rss.run()
