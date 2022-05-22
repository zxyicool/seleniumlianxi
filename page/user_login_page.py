# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/15 16:39
@Auth ： zxy
@File ：user_login_page.py

"""

from common.base import Base


class UserLoginPage(Base):
    user_loc = ('id', 'username')
    pwd_loc = ('id', 'password_l')
    log_btn_loc = ('id', 'jsLoginBtn')
    errorlist_loc = ('class name', 'errorlist')
    user_format_loc = ('id', 'jsLoginTips')

    def input_username(self, text):
        """输入用户名"""
        self.send(self.user_loc, text)

    def input_password(self, text):
        """输入密码"""
        self.send(self.pwd_loc, text)

    def click_login_btn(self):
        """点击登录按钮"""
        self.click(self.log_btn_loc)

    def get_login_errorlist(self):
        """获取登录错误信息"""
        return self.get_text(self.errorlist_loc)

    def get_login_format_error(self):
        """获取登录格式错误信息"""
        return self.get_text(self.user_format_loc)

