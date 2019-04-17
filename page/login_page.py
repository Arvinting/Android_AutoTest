# coding=utf-8
import page
from base.base import Base

"""
登录页面对象及方法封装
"""


class LoginPage(Base):

    def __init__(self, driver):
        Base.driver = driver

    def input_username(self, text):
        self.input_text(page.username, text)

    def input_password(self, text):
        self.input_text(page.password, text)

    def click_login_button(self):
        self.click_element(page.button_login)

    def confirm(self):
        self.click_element(page.confirm_button)
