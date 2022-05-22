# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/17 23:56
@Auth ： zxy
@File ：test_user_info.py

"""
import allure
import pytest
from page.user_info_page import UserInfoPage


@allure.feature('登录模块')
@allure.story('登录的测试用例')
class TestUserInfo():
    @pytest.fixture(autouse=True)
    def open_user_info(self, userInfoPage: UserInfoPage):
        userInfoPage.open('/users/userinfo/')

    @allure.title('修改昵称为空，点保存，提示：请输入昵称')
    def test_info_1(self, userInfoPage: UserInfoPage):
        """修改昵称为空，点保存，提示：请输入昵称！"""
        userInfoPage.clear_nickname_input()
        userInfoPage.input_nick_name('')
        userInfoPage.click_reserve_btn()
        assert userInfoPage.get_errortips_text() == '请输入昵称！'

    @pytest.mark.parametrize('test_input', ['上海悠悠', 'yoyo'],
                             ids=[
                                 '修改昵称：上海悠悠，点保存提示：个人信息修改成功',
                                 '修改昵称：yoyo，点保存提示：个人信息修改成功'
                             ])
    def test_info_2(self, userInfoPage: UserInfoPage, test_input):
        """修改昵称：上海悠悠，点保存提示：个人信息修改成功"""
        userInfoPage.clear_nickname_input()
        userInfoPage.input_nick_name(test_input)
        userInfoPage.click_reserve_btn()
        assert userInfoPage.get_dialog_text() == '个人信息修改成功！'

    @allure.title('修改昵称：yoyoabcdefg，大于10个字符，输入框最多显示10个字符')
    def test_info_3(self, userInfoPage: UserInfoPage):
        """修改昵称：yoyoabcdefg，大于10个字符，输入框最多显示10个字符"""
        userInfoPage.clear_nickname_input()
        userInfoPage.input_nick_name('yoyoabcdefg')
        userInfoPage.click_reserve_btn()
        assert userInfoPage.get_nickname_value() == 'yoyoabcdef'
