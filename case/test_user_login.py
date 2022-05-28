# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/15 16:48
@Auth ： zxy
@File ：test_user_login.py

"""

import pytest
from page.user_login_page import UserLoginPage


class TestUserLogin():

    @pytest.fixture(autouse=True)
    def open_user_login(self, userLoginPage: UserLoginPage):
        userLoginPage.open('/users/login/')

    def test_user_1(self, userLoginPage: UserLoginPage):
        """输入用户名为空，任意密码，点击登录按钮，提示：这个字段是必须的"""
        userLoginPage.input_username('')
        userLoginPage.input_password('11111')
        userLoginPage.click_login_btn()
        # 断言
        assert userLoginPage.get_login_errorlist() == '这个字段是必须的'

    def test_user_2(self, userLoginPage: UserLoginPage):
        """输入邮箱格式不正确123，密码123456，点登录按钮，提示用户名或密码错误"""
        userLoginPage.input_username('111111')
        userLoginPage.input_password('111111')
        userLoginPage.click_login_btn()
        # 断言
        assert userLoginPage.get_login_format_error() == '用户名或密码错误'

    def test_user_3(self, userLoginPage: UserLoginPage):
        """输入邮箱格式正确1234@qq.com，密码不对23456，点登录按钮，提示用户名或密码错误"""
        userLoginPage.input_username('1234@qq.com')
        userLoginPage.input_password('111111')
        userLoginPage.click_login_btn()
        # 断言
        assert userLoginPage.get_login_format_error() == '用户名或密码错误'

    def test_user_4(self, userLoginPage: UserLoginPage):
        """输入邮箱格式正确1234@qq.com，密码正确123456，点登录按钮，提示登录成功"""
        userLoginPage.input_username('1234@qq.com')
        userLoginPage.input_password('123456')
        userLoginPage.click_login_btn()
        # 断言
        assert userLoginPage.get_login_format_error() != '用户名或密码错误'

    def test_user_5(self, userLoginPage: UserLoginPage, base_url):
        """输入邮箱格式正确1234@qq.com，密码正确123456，点登录按钮，提示登录成功"""
        userLoginPage.input_username('1234@qq.com')
        userLoginPage.input_password('123456')
        userLoginPage.click_login_btn()
        # 断言判断跳转后的url
        assert userLoginPage.driver.current_url == base_url + '/'
