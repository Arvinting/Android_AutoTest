from selenium.webdriver.common.by import By

"""
首页面元素
"""
# 注册按钮
register_button = (By.ID, "com.tsingzone.questionbank:id/button_register")
# 登录按钮
login_button = (By.ID, "com.tsingzone.questionbank:id/button_login")

"""
登录页面元素
"""

# 账号
username = (By.ID, "com.tsingzone.questionbank:id/username")
# 密码
password = (By.ID, "com.tsingzone.questionbank:id/password")
# 登录按钮
button_login = (By.ID, "com.tsingzone.questionbank:id/button_login")
# 弹窗确定按钮
confirm_button = (By.ID, "android:id/button1")
# 弹窗信息
alert_message = (By.ID, "android:id/message")

"""
题库首页
"""

# 头像
userphoto = (By.ID, "com.tsingzone.questionbank:id/user_photo")
