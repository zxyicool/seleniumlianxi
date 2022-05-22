# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/10 21:56
@Auth ： zxy
@File ：test_register_new.py

"""
from page.register_page import RegisterPage
import pytest


class TestRegisterNew():

    @pytest.fixture(autouse=True)
    def open_register(self, registerPage: RegisterPage):
        registerPage.open('/users/register/')

    def test_email_1(self, registerPage: RegisterPage):
        """ 注册：输入邮箱，密码都为空，点提交按钮，两个输入框提示红色（class属性包含errorput）"""
        # registerPage.open('/users/register/')
        registerPage.input_email('')
        registerPage.input_password('')
        registerPage.click_register_btn()
        # 实际结果
        actual = registerPage.get_mail_class()
        # 断言
        assert 'errorput' in actual

    def test_email_2(self, registerPage: RegisterPage):
        """注册：输入邮箱格式不正确，密码为空，点提交按钮，邮箱输入框提示红色（class属性包含errorput）"""
        # registerPage.open('/users/register/')
        registerPage.input_email('1111')
        registerPage.input_password('')
        registerPage.click_register_btn()
        # 实际结果
        actual = registerPage.get_mail_class()
        # 断言
        assert 'errorput' in actual

    def test_password_3(self, registerPage: RegisterPage):
        """注册：邮箱格式正确，密码为空，点提交按钮，密码输入框提示红色（class属性包含errorput）"""
        # registerPage.open('/users/register/')
        registerPage.input_email('1111@.com')
        registerPage.input_password('')
        registerPage.click_register_btn()
        # 实际结果
        actual = registerPage.get_password_class()
        # 断言
        assert 'errorput' in actual

    def test_password_4(self, registerPage: RegisterPage):
        """注册：邮箱格式正确，密码小于6位，点提交按钮，密码输入框提示红色（class属性包含errorput）"""
        # registerPage.open('/users/register/')
        registerPage.input_email('1111@.com')
        registerPage.input_password('111')
        registerPage.click_register_btn()
        # 实际结果
        actual = registerPage.get_password_class()
        # 断言
        assert 'errorput' in actual

    def test_password_5(self, registerPage: RegisterPage):
        """注册：邮箱格式正确，密码大于20位，点提交按钮，密码输入框提示红色（class属性包含errorput）"""
        # registerPage.open('/users/register/')
        registerPage.input_email('11101@.com')
        registerPage.input_password('1111111111111111111111111')
        registerPage.click_register_btn()
        # 实际结果
        actual = registerPage.get_password_class()
        # 断言
        assert 'errorput' in actual

    def test_email_input_6(self, registerPage: RegisterPage):
        """输入文本：1111@qq.com再清空文本"""
        registerPage.input_email('1111@qq.com')
        actual = registerPage.get_email_attr(attr="value")
        assert actual == '1111@qq.com'
        # 清空
        registerPage.clear_email_input()
        assert registerPage.get_email_attr(attr="value") == ''

    def test_password_input_7(self, registerPage: RegisterPage):
        """输入文本：1111再判断是否显示****"""
        registerPage.input_password('1111')
        actual = registerPage.get_password_attr(attr="value")
        assert actual == '1111'
        assert registerPage.get_password_attr(attr="type") == 'password'

    def test_register_link_8(self, registerPage: RegisterPage, base_url):
        """点回到首页，跳转到首页"""
        actual = registerPage.get_link_href('//*[@class="index-font"]')
        assert actual == base_url+'/'



