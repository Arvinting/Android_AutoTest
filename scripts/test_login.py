import sys, os

sys.path.append(os.getcwd())

import pytest, allure
import page
from page.page import Page_Obj
from base.read_yaml_data import ReadYaml
from base.init_driver import init_driver

def get_login_data():
    data_list = []
    login_data = ReadYaml('login_data').read_data()
    for i in login_data.keys():
        data_list.append((i, login_data.get(i).get('username'), login_data.get(i).get('password')))
    return data_list

class Test_Login:

    def setup_class(self):
        self.driver = init_driver()
        self.login_obj = Page_Obj(self.driver).login_page_obj()
        self.login_obj.click_element(page.login_button)

    def teardown_class(self):
        self.driver.quit()
    @allure.step('测试登录')
    @pytest.mark.parametrize("testcase, username, password", get_login_data())
    def test_login(self, testcase, username, password):
        print(testcase)
        self.login_obj.input_username(username)
        self.login_obj.input_password(password)
        self.login_obj.click_login_button()
        self.login_obj.confirm()

