# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/17 23:22
@Auth ： zxy
@File ：user_info_page.py

"""

from common.base import Base
import time


class UserInfoPage(Base):
    nick_name_loc = ('id', 'nick_name')
    jsEditUserBtn_loc = ('id', 'jsEditUserBtn')
    error_tips_loc = ('class name', 'error-tips')
    jsSuccessTips_dialog_loc = ('xpath', '//*[@id="jsSuccessTips"]/div[2]')

    def clear_nickname_input(self):
        """清空昵称输入框"""
        self.clear(self.nick_name_loc)

    def input_nick_name(self, name=''):
        """输入要修改的昵称"""
        self.send(self.nick_name_loc, name)

    def click_reserve_btn(self):
        """点击保存按钮"""
        self.click(self.jsEditUserBtn_loc)

    def get_errortips_text(self):
        """获取错误文本"""
        return self.get_text(self.error_tips_loc)

    def get_dialog_text(self):
        """获取dialog文本"""
        time.sleep(0.2)
        return self.get_text(self.jsSuccessTips_dialog_loc)

    def get_nickname_value(self):
        """获取输入框文本"""
        return self.get_attribute(self.nick_name_loc, 'value')