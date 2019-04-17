from selenium.webdriver.support.wait import WebDriverWait


class Base:

    def __init__(self, driver):
        self.driver = driver

    def find_single_element(self, loc, timeout=10, poll=0.5):
        """
        封装元素查找显示等待方法
        :param loc: 传入定位方式及元素信息的元组， 如(By.ID, "com.tsingzone.questionbank:id/button_register")
        :param timeout: 等待超时时间，默认为10秒
        :param poll: 轮询时间，默认为0.5秒
        :return: 返回元素对象
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))
    
    def click_element(self, loc):
        """
        封装元素点击方法
        :param loc: 传入定位方式及元素信息的元组， 如(By.ID, "com.tsingzone.questionbank:id/button_register")
        """
        self.find_single_element(loc).click()

    def input_text(self, loc, text):
        """
        封装元素输入文本值方法（先清空再输入）
        :param loc: 传入定位方式及元素信息的元组， 如(By.ID, "com.tsingzone.questionbank:id/button_register")
        :param text: 传入需输入的文本值
        """
        ele = self.find_single_element(loc)
        ele.clear()
        ele.send_keys(text)

