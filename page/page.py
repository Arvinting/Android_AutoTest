from page.login_page import LoginPage
from page.question_page import QuestionPage

"""
统一页面入口
"""


class PageObj(object):
    def __init__(self, driver):
        self.driver = driver

    # 登录页面对象
    def login_page_obj(self):
        return LoginPage(self.driver)

    # 题库页面对象
    def question_page_obj(self):
        return QuestionPage(self.driver)

