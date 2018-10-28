# coding=utf8
import json
import threading
from time import sleep, time


class Information():
    # 构造函数,关于基本配置,文件读档
    def __init__(self, last_time):
        # 数据成员
        self.stack = {}  # 存储技术栈信息

        # 从文件中，读取技术栈数据
        try:
            with open('stack.json') as f:
                self.stack = json.load(f)
        except:
            self.stack = {}


info = Information(time())


def wait():
    while (True):
        sleep(5)
        with open('stack.json', 'w') as f: f.write(json.dumps(info.stack, ensure_ascii=False))


t = threading.Thread(target=wait)  # 多线程计算时间五分钟
t.setDaemon(True)  # 后台进程,定时操作
t.start()
