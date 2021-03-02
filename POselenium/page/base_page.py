from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# 基类，存放都需要用到的方法
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    base_url = ""

    # 封装init方法
    def __init__(self, driver: webdriver = None):
        # 如果driver是空的，则复用浏览器，如果不是空的，则使用当前的driver
        if driver is None:
            # 复用浏览器，使用option.debugger_address
            option = Options()
            option.debugger_address = '127.0.0.1:9222'
            self.driver = webdriver.Chrome(options=option)
        else:
            self.driver = driver
        # 如果网址不是空的，则跳转到输入的网站
        if self.base_url != "":
            self.driver.get(self.base_url)
        # 隐式等待
        self.driver.implicitly_wait(5)

    # 封装定位单个元素的方法
    def find(self, local, value):
        return self.driver.find_element(local, value)

    # 封装定位单个元素的方法
    def finds(self, local, value):
        return self.driver.find_elements(local, value)

    # 封装显示等待
    def wait(self,timeout,local):
        WebDriverWait(self.driver,timeout).until(expected_conditions.element_to_be_clickable(local))
