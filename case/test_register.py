# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/6 23:25
@Auth ： zxy
@File ：test_register.py
@IDE ：PyCharm

"""
from page.register_page import RegisterPage


class TestRegister():
    # def test_register_success(self, driver, base_url):
    #     """注册成功的用例"""
    #     register = RegisterPage(driver, base_url)
    #     register.open('/users/register/')
    #     # 操作步骤
    #     register.input_email('101011@qq.com')
    #     register.input_password('101010')
    #     register.click_register_btn()
    #     # 实际结果
    #     actual_result = register.register_success_text()
    #     # 断言
    #     assert actual_result == '尊敬的用户，您好，账户已激活成功！'

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
