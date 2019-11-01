"""
通过api.gushi.ci 获取古诗词
"""
import ast
import random

import requests
from bs4 import BeautifulSoup


class Juzi(object):
    """
    获取各种句子
    """
    def getshici(self):
        """
        获取古诗词
        :return:
        """
        r = requests.get("https://api.gushi.ci/all.json")
        return r.content

    def getdujitang(self):
        """
        获取毒鸡汤
        :return:
        """
        r = requests.get("http://nows.fun")
        html_r = BeautifulSoup(r.text, 'html.parser')
        r = html_r.span
        return r.text

    def getonesentence(self):
        """
        从文件 result_4 中随机获取一句话
        """
        num = random.randrange(0, 2546)
        file = open('/opt/smsweather/juzi/result_4.txt', 'rb')
        sentence = file.readlines()[num].decode('utf-8')
        sen = dict(ast.literal_eval(sentence))
        file.close()
        return sen['setence']


def main():
    """
    入口
    """
    test = Juzi()
    r = test.getonesentence()
    print(r)


if __name__ == '__main__':
    main()
