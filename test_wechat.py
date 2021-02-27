from optparse import Option
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestWeChat():

    def setup(self):
        # 复用已登录企业微信的浏览器，获取带有登录的cookie
        # option = Options()
        # option.debugger_address = '127.0.0.1:9222'
        # self.driver = webdriver.Chrome(options=option)
        # 获取cookie后可直接打开新的浏览器
        self.driver = webdriver.Chrome()
        # 隐式等待5秒
        self.driver.implicitly_wait(5)

    def teardown(self):
        # 退出浏览器
        self.driver.quit()

    def test_wechat(self):
        # 进入已登录的企业微信
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 获取cookie
        # cookies = self.driver.get_cookies()
        # sleep(3)
        # print(cookies)
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # sleep(3)
        # 含有登录信息的cookie
        cookies =[{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688854145126139'},
                  {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'yp47uoBH3DpYmnOouS6gDuyPKRxvi41ylwncAXnAVTUwGb6Mihfi-po0nP0M5xokwQXzEYokQl5HmUql4BTfhXQ6ykjsIGdx8jOKKWB4RgYAH7xrKDuNf2bIdouQRPr0U9CUkiloFNUALKaJAFaQCq11gjB4X5wrpi53p9ZYKNTmi4XuTjPhbejv2FcvKOLO3_LtnG0XNFhMXUKsSin2Rh2QgW4sHD9d2eDA2bV-Z6ZqD4AN7hBnHnFRPdywM0eVWZheE1sfi5QbkXQuXDl__g'},
                  {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688854145126139'},
                  {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324955424119'},
                  {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'IiRTWSZJbUKNU2WLpemZI1fRfuKcwXTJiXgr_UN7QG1qU0_aOsRmjgZ1yX-kuQgd'},
                  {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a5783682'},
                  {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'},
                  {'domain': '.work.weixin.qq.com', 'expiry': 1645848954, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1614244011,1614310459,1614312716,1614312954'},
                  {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'},
                  {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1614312954'},
                  {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '3823160028949182'},
                  {'domain': '.qq.com', 'expiry': 1614399374, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1084792093.1614243893'},
                  {'domain': 'work.weixin.qq.com', 'expiry': 1614341994, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '4fuqlv8'},
                  {'domain': '.qq.com', 'expiry': 1614313014, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'},
                  {'domain': '.qq.com', 'expiry': 1677384974, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.477639929.1614243893'},
                  {'domain': '.work.weixin.qq.com', 'expiry': 1645779892, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'},
                  {'domain': '.work.weixin.qq.com', 'expiry': 1616905002, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}]
        # 遍历cookie
        for cookie in cookies:
            # 如果expire字段在cookie中，则移除它
            if 'expire' in cookie.keys():
                cookie.pop()
            # 在浏览器中加入cookie
            self.driver.add_cookie(cookie)
        # 打开带有cookie的浏览器
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 定位到导入通讯录按钮并点击
        self.driver.find_element_by_css_selector('.index_service_cnt_itemWrap:nth-child(2)').click()
        # 定位到上传文件按钮并指定通讯录路径进行上传
        self.driver.find_element_by_id('js_upload_file_input').send_keys('C:/Users/86185/Desktop/通讯录.xlsx')
        # 断言通讯录的名称是否与上传文件名称一致
        assert '通讯录.xlsx' == self.driver.find_element_by_id('upload_file_name').text
        # 定位到确定导入按钮并点击
        self.driver.find_element_by_id('submit_csv').click()
        # 断言是否上传成功，定位到前往查看按钮，查看此按钮是否存在
        assert '前往查看' == self.driver.find_element_by_id('reloadContact').text
        # 点击前往查看按钮
        self.driver.find_element_by_id('reloadContact').click()




