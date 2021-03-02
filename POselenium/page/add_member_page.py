from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_selenium.POselenium.page.base_page import BasePage


class AddMemberPage(BasePage):
    # # 实例化并使用主页的driver
    # def __init__(self, driver: webdriver):
    #     self.driver = driver

    # 添加成员页面
    def add_member_page(self,username,account,phonenumber):
        # 定位到用户名输入框并输入内容
        self.find(By.CSS_SELECTOR,".ww_compatibleTxt_ipt").send_keys(username)
        # 定位到用户账号输入框并输入内容
        self.find(By.ID,"memberAdd_acctid").send_keys(account)
        # 定位到用户号码输入框并输入内容
        self.find(By.ID,"memberAdd_phone").send_keys(phonenumber)
        # 定位到保持按钮并点击
        self.find(By.CSS_SELECTOR,".js_btn_save").click()
        #self.driver.find_element(By.LINK_TEXT, "保存").click()
        return True

    # 添加成员成功,获取所有成员姓名
    def add_member_successful(self):
        # 显示等待
        #WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,".member_colRight_memberTable_td_Checkbox")))
        self.wait(10,(By.CSS_SELECTOR,".member_colRight_memberTable_td_Checkbox"))
        # find_elements 查找页面上的相同属性的所有元素
        # 获取所有成员姓名，得到的是列表
        member_names_list = self.finds(By.CSS_SELECTOR,".member_colRight_memberTable_td:nth-child(2)")
        # 获取所有成员姓名的title属性
        for ele in member_names_list:
            member_names = ele.get_attribute("title")
        return member_names