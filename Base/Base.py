from selenium.webdriver.support.wait import WebDriverWait


class Base:

    def __init__(self, driver):
        self.driver = driver

    def find_single_element(self, loc, timeout=10, poll=0.5):
        """

        :param loc:
        :param timeout:
        :param poll:
        :return:
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))
    
    def click_element(self, loc):
        """

        :param loc:
        :return:
        """
        self.find_single_element(loc).click()

    def input_text(self, loc, text):
        """

        :param loc:
        :param text:
        :return:
        """
        ele = self.find_single_element(loc)
        ele.clear()
        ele.send_keys(text)