from base.base import Base


class QuestionPage(Base):

    def __init__(self, driver):
        Base.driver = driver
