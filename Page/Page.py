from Page.login_page import Login_page


class Page_Obj:
    def __init__(self, driver):
        self.driver = driver
    def login_page_obj(self):
        return Login_page(self.driver)
