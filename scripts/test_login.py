import sys
import os

sys.path.append(os.getcwd())

import pytest
import allure
import page
from base.init_driver import init_driver
from page.page import PageObj
from utils.read_yaml_data import ReadYaml


def get_login_data():
    data_list = []
    login_data = ReadYaml('login_data').read_data()
    for i in login_data.keys():
        data_list.append(
            (i, login_data.get(i).get('flag'), login_data.get(i).get('username'), login_data.get(i).get('password'),
             login_data.get(i).get('message')))
    return data_list


class TestLogin(object):

    def setup_class(self):
        self.driver = init_driver()
        self.login_obj = PageObj(self.driver).login_page_obj()
        self.question_obj = PageObj(self.driver).question_page_obj()
        self.login_obj.click_element(page.login_button)

    def teardown_class(self):
        self.driver.quit()

    @allure.step('测试登录流程')
    @pytest.mark.parametrize("case, flag, username, password, message", get_login_data())
    def test_login(self, case, flag, username, password, message):
        if flag == 1:
            print(case)
            self.login_obj.input_username(username)
            self.login_obj.input_password(password)
            self.login_obj.click_login_button()
            actual = self.login_obj.find_single_element(page.alert_message).text
            self.login_obj.confirm()
            assert actual == message
        if flag == 2:
            print(case)
            self.login_obj.input_username(username)
            self.login_obj.input_password(password)
            actual = self.login_obj.find_single_element(page.button_login).is_enabled()
            assert actual == False
        if flag == 3:
            print(case)
            self.login_obj.input_username(username)
            self.login_obj.input_password(password)
            self.login_obj.click_login_button()
            actual = self.question_obj.find_single_element(page.userphoto).is_enabled()
            assert actual == True
