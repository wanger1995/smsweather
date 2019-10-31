"""
爬取天气，发送短信
"""
import time

import requests
from lxml import etree
from twilio.rest import Client  # 用于短信接口，需要安装twilio库，安装方法:pip install twilio
from yiyan.juzi import juzi

'''功能，每天发送今日天气给ta'''


# 东莞 101281601
# 达州 101270601


def message():
    """
    爬取天气，
    :param
    :return:
    """
    url = 'https://tianqi.so.com/weather/101281601'
    html = requests.get(url)
    if html.status_code == 200:
        htmltext = html.text
        htmlxpath = etree.HTML(htmltext)
        weather = htmlxpath.xpath('//*[@id="weather-alarm"]/div[2]/div[1]/div[1]/div[1]/p[1]/text()')[0]  # 天气
        body = htmlxpath.xpath('//*[@id="weather-alarm"]/div[2]/div[1]/div[1]/div[1]/p[2]/text()')[0]  # 温度
        wind = htmlxpath.xpath('//*[@id="weather-alarm"]/div[2]/div[1]/div[1]/div[1]/p[3]/text()')[0]  # 风向
        windstrong = htmlxpath.xpath('//*[@id="weather-alarm"]/div[2]/div[1]/div[1]/div[1]/p[4]/text()')[0]  # 风力
        humidity = htmlxpath.xpath('//*[@id="weather-alarm"]/div[2]/div[1]/div[1]/div[1]/p[6]/text()')[0]  # 湿度
        guomin = htmlxpath.xpath('//*[@id="china-weather"]/div[2]/div[4]/div[2]/div[1]/div[1]/div[2]')[0].attrib.get(
            'title')  # 过敏
        fangsai = htmlxpath.xpath('//*[@id="china-weather"]/div[2]/div[4]/div[2]/div[1]/div[5]/div[2]/text()')[0]
        chuanyi = htmlxpath.xpath('//*[@id="china-weather"]/div[2]/div[4]/div[2]/div[1]/div[2]/div[2]/text()')[0]  # 穿衣
        fangbin = htmlxpath.xpath('//*[@id="china-weather"]/div[2]/div[4]/div[2]/div[1]/div[4]/div[2]/text()')[0]  # 感冒
        daisan = htmlxpath.xpath('//*[@id="china-weather"]/div[2]/div[4]/div[2]/div[1]/div[8]/div[2]/text()')[0]  # 降雨
        c = juzi.Juzi()
        jitang = c.getonesentence()
        # jitang = '也许只要还有人在不断想念，逝去的人就并没有真的离开吧。'
        sedtext = '强哥，早上好啊' + \
                  jitang + '\n' + \
                  '天气:' + weather + '\n' + \
                  '温度:' + body + '\n' + \
                  '风向:' + wind + '\n' + \
                  '风力:' + windstrong + '\n' + \
                  '过敏：' + guomin + '\n' + \
                  '防晒：' + fangsai + '\n' + \
                  '穿衣:' + chuanyi + '\n' + \
                  '防病:' + fangbin + '\n' + \
                  '降雨:' + daisan

        return sedtext


def sedsms(text, userphone):
    """
    发送短信
    :return:
    """
    sid = 'AC4747d3206b49395bb5ab33d157bcaf1b'  # 你自己的sid
    token = '61d7b49b3eb8d198a62eac9fbb26d26e'  # 你自己的token
    client = Client(sid, token)
    # body就是我们定义的短信内容，from是网站给你分配的一个虚拟手机号，to是表示发送短信给谁
    message = client.messages.create(body=text, from_='+13155440904', to=userphone)
    # time.sleep(1)
    # message = client.messages.create(body=text, from_='+13155440904', to=xyr)
    print(message.sid)


def main():
    """

    :return:
    """
    hjf = '+8617745446935'
    xyr = '+8618781673651'
    lyl = '+8619982064824'
    hzq = '+8618603036124'
    user_list = [hzq, hjf]
    for i in user_list:
        text = message()
        sedsms(text, i)


if __name__ == '__main__':  # 程序入口
    main()
