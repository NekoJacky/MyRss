import json
import os


class Config:
    def __init__(self, bilibili):
        self.bilibili = []
        # print(self.bilibili)
        for user in bilibili:
            self.bilibili.append(Bilibili(user['user_phone'], user['password']))

    # Test
    def print_obj(self):
        for bilibili in self.bilibili:
            print(bilibili.user_phone, bilibili.password)


class Bilibili:
    def __init__(self, user_phone, password):
        self.user_phone = user_phone
        self.password = password


def json_to_config(config_str):
    return Config(config_str['bilibili'])


class ConfigParser:
    def __init__(self):
        if not os.path.exists('config.json'):
            user_phone = input('input your phone number: ')
            password = input('input your password: ')
            config_dict = {
                "bilibili": [
                    {
                        "user_phone": user_phone,
                        "password": password
                    }
                ]
            }
            with open('config.json', 'w') as f:
                json.dump(config_dict, f, ensure_ascii=False, indent=4)
            f.close()
        self.config_str = json.load(open('config.json'))
        # print(config_str, type(config_str))

    def parse(self):
        return json_to_config(self.config_str)


if __name__ == '__main__':
    parser = ConfigParser()
    config = parser.parse()
    # print(cfg)
    config.print_obj()
