# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/15 18:52
@Auth ： zxy
@File ：user_feedbackiframe_page.py

"""

from common.base import Base


class FeedbackPage(Base):
    feedback_iframe_loc = ('id', 'feedback_iframe')
    feedback_select_loc = ('name', 'subject')
    feedback_content_loc = ('id', 'mesaage')
    feedback_relate_loc = ('name', 'message')
    # feedback_relate_loc = ('xpath', '//*[@class="blur"]//input')
    feedback_send_btn = ('class name', 'button')

    def to_iframe(self):
        """切换到iframe界面"""
        self.switch_iframe(self.feedback_iframe_loc)

    def select_subject(self, value=''):
        """获取选中的下拉框选项"""
        self.select_by_value(self.feedback_select_loc, value)

    def input_feedback_content(self, text=''):
        """输入反馈内容"""
        self.send(self.feedback_content_loc, text)

    def input_feedback_relate(self, text=''):
        """输入联系方式"""
        self.send(self.feedback_relate_loc, text)

    def click_send_btn(self):
        """点击发送按钮"""
        self.click(self.feedback_send_btn)

    def get_select_object(self):
        """获取select所有选项"""
        all_options = self.select_object(self.feedback_select_loc).options
        all_text = [i.text for i in all_options]
        return all_text

    def selected_subject(self, value=''):
        """获取被选中的第一个选项"""
        selected = self.select_object(self.feedback_select_loc).first_selected_option
        return selected.text

    def get_relate_attr(self, attr='value'):
        """获取联系我们输入框属性，默认获取value属性"""
        return self.get_attribute(self.feedback_relate_loc, attr)


