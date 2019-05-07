# coding=utf-8
from appium import webdriver

"""
定义初始化driver方法
"""


def init_driver():

    desired_caps = {}
    # 使用平台
    desired_caps['platformName'] = 'Android'
    # 设备号
    desired_caps['deviceName'] = 'R3E0216607000851'
    # 系统版本号
    desired_caps['platformVersion'] = '6.0'
    # APP包名
    desired_caps['appPackage'] = 'com.tsingzone.questionbank'
    # APP入口activity
    desired_caps['appActivity'] = 'com.yiqischool.activity.YQHomeActivity'
    # 输入中文需设置以下两个参数
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # 启动APP重置数据
    desired_caps['noReset'] = False
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver
