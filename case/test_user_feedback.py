# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/16 20:39
@Auth ： zxy
@File ：test_user_feedback.py

"""
import pytest
from page.user_feedbackiframe_page import FeedbackPage


class TestFeedback():

    @pytest.fixture(autouse=True)
    def open_feedback(self, userFeedbackPage: FeedbackPage):
        userFeedbackPage.open('/users/feedbackiframe/')
        userFeedbackPage.to_iframe()

    def test_all_option_1(self, userFeedbackPage: FeedbackPage):
        """获取所有下拉选项"""
        all_options = userFeedbackPage.get_select_object()
        print(all_options)
        assert all_options == ['改进建议', '页面布局', '提BUG']

    def test_selected_option_2(self, userFeedbackPage: FeedbackPage):
        """获取被选中项"""
        userFeedbackPage.select_subject(value='页面布局')
        assert userFeedbackPage.selected_subject(value='页面布局') == '页面布局'
        userFeedbackPage.select_subject(value='改进建议')
        assert userFeedbackPage.selected_subject(value='改进建议') == '改进建议'
        userFeedbackPage.select_subject(value='提BUG')
        assert userFeedbackPage.selected_subject(value='提BUG') == '提BUG'

    def test_contract_clear_3(self, userFeedbackPage: FeedbackPage):
        """输入联系方式 1111@qq.com再清空"""
        userFeedbackPage.input_feedback_relate('111111@qq.com')
        actual = userFeedbackPage.get_relate_attr(attr='value')
        assert actual == '111111@qq.com'

    @pytest.mark.parametrize('test_input', ['改进建议', '页面布局', '提BUG'])
    def test_selected_option_4(self, userFeedbackPage: FeedbackPage, test_input):
        """获取被选中项,参数化"""
        userFeedbackPage.select_subject(value=test_input)
        assert userFeedbackPage.selected_subject(value='页面布局') == test_input

    def test_feedback_send_5(self, userFeedbackPage: FeedbackPage):
        """改进建议，反馈内容为空，测试内同为空，点send提交按钮，alert弹窗提示：提交成功"""
        # 选改进建议
        userFeedbackPage.select_subject(value='页面布局')
        # 写反馈内容
        userFeedbackPage.input_feedback_content('')
        # 写联系方式
        userFeedbackPage.input_feedback_relate('')
        # 点确定按钮
        userFeedbackPage.click_send_btn()
        # 获取alert结果并断言
        text = userFeedbackPage.get_alert_text()
        assert text == '提交成功！'

    @pytest.mark.parametrize('test_input, expected', [
        [{'subject': '改进建议', 'content': '', 'relate': ''}, '提交成功！'],
        [{'subject': '改进建议', 'content': 'test', 'relate': ''}, '提交成功！'],
        [{'subject': '改进建议', 'content': '', 'relate': '111111@qq.com'}, '提交成功！'],
        [{'subject': '改进建议', 'content': 'test', 'relate': '111111@qq.com'}, '提交成功！'],
        [{'subject': '页面布局', 'content': 'test', 'relate': '111111@qq.com'}, '提交成功！'],
        [{'subject': '提BUG', 'content': 'test', 'relate': '111111@qq.com'}, '提交成功！'],
    ])
    def test_feedback_send_6(self, userFeedbackPage: FeedbackPage, test_input, expected):
        """参数化 改进建议，反馈内容为空，测试内同为空，点send提交按钮，alert弹窗提示：提交成功"""
        # 选改进建议
        userFeedbackPage.select_subject(value=test_input['subject'])
        # 写反馈内容
        userFeedbackPage.input_feedback_content(test_input['content'])
        # 写联系方式
        userFeedbackPage.input_feedback_relate(test_input['relate'])
        # 点确定按钮
        userFeedbackPage.click_send_btn()
        # 获取alert结果并断言
        text = userFeedbackPage.get_alert_text()
        assert text == expected
