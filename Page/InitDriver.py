from appium import webdriver


def init_driver():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['deviceName'] = 'R3E0216607000851'
    desired_caps['platformVersion'] = '6.0'
    desired_caps['appPackage'] = 'com.tsingzone.questionbank'
    desired_caps['appActivity'] = 'com.yiqischool.activity.YQHomeActivity'
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    desired_caps['noReset'] = False
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver
