from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from test_selenium.POselenium.page.add_member_page import AddMemberPage
from test_selenium.POselenium.page.base_page import BasePage


class MainPage(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame"
    # 跳转至添加成员界面
    def goto_add_member(self):
        # 定位到添加成员按钮并点击
        self.find(By.CSS_SELECTOR,".index_service_cnt_itemWrap:nth-child(1)").click()
        # 跳转到添加成员页面
        return AddMemberPage(self.driver)

