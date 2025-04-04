import json
from datetime import datetime
from typing import cast


class Config:
    def __init__(self):
        self.bilibili_config = BilibiliConfig()

    def get_bilibili_config(self) -> dict:
        return self.bilibili_config.get_bilibili_config()

    def add_bilibili_config(self) -> None:
        self.bilibili_config.add_bilibili_config()

    def delete_bilibili_config(self) -> None:
        self.bilibili_config.delete_bilibili_config()

    def change_bilibili_config(self) -> None:
        self.bilibili_config.change_bilibili_config()


class BilibiliConfig:
    def __init__(self):
        try:
            with open('config.json', 'r', encoding='utf-8') as json_data:
                self.config = json.load(json_data)
        except FileNotFoundError:
            self.config = {}

    def save_config(self) -> None:
        with open('config.json', 'w', encoding='utf-8') as json_data:
            json.dump(self.config, cast("SupportsWrite[str]", json_data), ensure_ascii=False, indent=4)

    def get_exist_phone(self) -> str:
        phone = input('输入电话号码')
        while phone not in self.config['bilibili']:
            phone = input('不存在电话信息，重新输入电话号码')
        return phone

    def get_new_phone(self) -> str:
        phone = input('输入电话号码')
        if 'bilibili' in self.config:
            while phone in self.config['bilibili']:
                phone = input('电话已存在，重新输入电话号码')
        return phone

    def get_bilibili_config(self) -> dict:
        bilibili_config = {}
        if 'bilibili' in self.config:
            bilibili_config = self.config['bilibili']
        return bilibili_config

    def add_bilibili_config(self) -> None:
        phone = self.get_new_phone()
        password = input('输入密码')
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        user_config = {'password': password, 'last_update_time': time}
        if 'bilibili' in self.config:
            self.config['bilibili'][phone] = user_config
        else:
            self.config['bilibili'] = {phone: user_config}
        self.save_config()

    def delete_bilibili_config(self) -> None:
        if 'bilibili' not in self.config:
            print('不存在用户信息')
            return
        phone = self.get_exist_phone()
        self.config['bilibili'].pop(phone)

    def change_bilibili_config(self) -> None:
        if 'bilibili' not in self.config:
            print('不存在用户信息')
            return
        phone = self.get_exist_phone()
        password = input('输入密码')
        self.config['bilibili'][phone]['password'] = password
        self.save_config()


if __name__ == '__main__':
    config = Config()
    print('----------')
    config_str = config.get_bilibili_config()
    print(config_str)
    # print('----------')
    # config.add_bilibili_config()
    print('----------')
