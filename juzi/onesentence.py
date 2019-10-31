"""
根据wechatsogou 获取人民日报的新闻早班车语录
"""
import time

import wechatsogou
import requests
from bs4 import BeautifulSoup
import json
from multiprocessing.pool import Pool


def get_pages(url):
    """
    获取one的网页
    :return:
    """
    result_dict = {}
    url_pre = 'http://wufafuwu.com'

    page = requests.get(url).content
    soup = BeautifulSoup(page, 'html.parser')
    for i in soup.find_all('li', class_='photo-big'):

        # 图片地址
        image = i.find_all('img')[0].get('src')
        # print(image)
        imagesurl = url_pre
        for j in image:
            imagesurl += j
        # 获取具体某天的地址
        sentenceurl = url_pre + i.find_all('a')[0].get('href')
        # 句子

        setence = get_sentence(sentenceurl)

        # 按空格分割只取有用的
        yield {
            'imageyrl': imagesurl,
            'setence': setence
        }


def get_sentence(url):
    """

    :param url:
    :return:
    """
    page_1 = requests.get(url).content
    soup_1 = BeautifulSoup(page_1, 'html.parser')
    for i in soup_1.find_all('div', class_='one-cita'):
        return i.text.strip()


def write_to_file(content):
    """

    :param content:
    """
    with open('result_4.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main(offset):
    """
    主程序
    """
    url = "http://wufafuwu.com/a/ONE_tupian/"
    url_1 = url + 'list_11_' + str(offset) + '.html'
    for item in get_pages(url_1):
        # pass
        write_to_file(item)
    # url = 'http://wufafuwu.com/a/ONE_tupian/2015/0710/3601.html'
    # s = get_sentence(url)


GROUP_START = 1
GROUP_END = 213
if __name__ == '__main__':
    # main()
    pool = Pool(processes=10)
    groups = []
    for x in range(GROUP_START, GROUP_END + 1):
        groups.append(x)
    print("开始获取")
    pool.map(main, groups)
    pool.close()
    pool.join()
    print("获取结束")
