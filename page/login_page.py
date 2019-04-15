from base.base import Base
import page


class Login_page(Base):

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
