"""
自动发送短信
每天早上7点
"""
import time
import os
import subprocess
import sys
import logging

# 本程序用于创建定时任务，个人觉得windows上面的定时任务创建不方便
# 到了某个时间，需要执行某个程序，非常像一个字典，所以我们这两个变量封装在字典里
# 格式为：'时间':'脚本的路径'
timeprocess = {
    '2050': 'E:\\pystudy\\spider\\study-book\\smstoyou.py',
    '2049': 'C:\\Windows\\SysWOW64\\calc.exe',
}


# 获取当前系统时间，精确到分时，例0810
def getnowtime():
    """

    :return:
    """
    nowtime = time.strftime('%H%M', time.localtime())
    print(nowtime)
    return nowtime


# 获取当前系统的python.exe文件路径
def getpythonpath():
    """

    :return:
    """
    path = 'C:\\Users\\yss\\AppData\\Local\\Programs\\Python\\Python37\\python.exe'
    return path


# 当前时间等于我们定义的字典中的时间时，我们就执行相应的py程序
def perform(getnowtimes):
    """

    :return:
    """
    for t, p in timeprocess.items():
        if getnowtimes == t:
            if p.endswith('.py'):
                subprocess.Popen(['%s' % getpythonpath(), p])
            elif p.endswith('.exe'):
                subprocess.Popen(p)
            else:
                print('程序不合法，即不是python文件，也不是exe文件')


if __name__ == '__main__':
    # print(getpythonpath())
    while True:
        t = getnowtime()
        perform(t)
        time.sleep(35)
