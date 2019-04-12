from Base.Base import Base
import Page


class Login_page(Base):

    def __init__(self, driver):
        Base.driver = driver

    def input_username(self, text):
        self.input_text(Page.username, text)

    def input_password(self, text):
        self.input_text(Page.password, text)

    def click_login_button(self):
        self.click_element(Page.button_login)
