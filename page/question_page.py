from base.base import Base

"""
题库首页面对象及方法封装
"""


class QuestionPage(Base):

    def __init__(self, driver):
        Base.driver = driver
