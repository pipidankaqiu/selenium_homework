from test_selenium.POselenium.page.main_page import MainPage


class TestAddMember():
    def setup(self):
        self.mainpage = MainPage()

    def test_add_member(self):
        # 传入用户名、账号、手机号码的参数
        username = "005"
        account = "005"
        phonenumber = "15555555555"
        # 通过主页点击添加成员跳转至添加成员界面
        page = self.mainpage.goto_add_member()
        # 通过添加成员界面的添加成员方法，成功添加成员
        page.add_member_page(username,account,phonenumber)
        # 通过添加成员界面的添加成员成功的方法，获取所有成员名称
        member_names = page.add_member_successful()
        # 断言传入的用户名是否在所有成员名称中
        assert username in member_names