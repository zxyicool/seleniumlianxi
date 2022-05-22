# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/15 15:08
@Auth ： zxy
@File ：test_register_db.py

"""

from page.register_page import RegisterPage
import pytest


class TestRegister():
    @pytest.fixture()
    def delete_user(self, db):
        sql = "DELETE  from users_userprofile where username = '101011@qq.com'"
        db.execute(sql)

    def test_register_success(self, driver, base_url, delete_user):
        """注册成功的用例"""
        register = RegisterPage(driver, base_url)
        register.open('/users/register/')
        # 操作步骤
        register.input_email('101011@qq.com')
        register.input_password('101010')
        register.click_register_btn()
        # 实际结果
        actual_result = register.register_success_text()
        # 断言
        assert actual_result == '尊敬的用户，您好，账户已激活成功！'

    def test_register_exited(self, driver, base_url):
        '''注册成功的用例'''
        register = RegisterPage(driver, base_url)
        register.open('/users/register')
        # 操作步骤
        register.input_email('1010@qq.com')
        register.input_password('101010')
        register.click_register_btn()
        # 实际结果
        actual_result = register.register_success_text()
        # 断言
        assert actual_result != '尊敬的用户，您好，账户已激活成功！'
