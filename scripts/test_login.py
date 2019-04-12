import sys, os
sys.path.append(os.getcwd())

from Page.Page import Page_Obj
import pytest
import Page
from Page.InitDriver import init_driver

class Test_Login:

    def setup_class(self):
        self.driver = init_driver()
        self.login_obj = Page_Obj(self.driver).login_page_obj()
        self.login_obj.click_element(Page.login_button)

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.parametrize("username, password", [(1231312321, 21313123123), (213133, 12312321)])
    def test_login(self, username, password):
        self.login_obj.input_username(username)
        self.login_obj.input_password(password)
        self.login_obj.click_login_button()

