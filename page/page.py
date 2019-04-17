from page.login_page import LoginPage
from page.question_page import QuestionPage


class PageObj(object):
    def __init__(self, driver):
        self.driver = driver

    def login_page_obj(self):
        return LoginPage(self.driver)

    def question_page_obj(self):
        return QuestionPage(self.driver)

