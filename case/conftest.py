# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/9 22:11
@Auth ： zxy
@File ：conftest.py
@IDE ：PyCharm

"""
import pytest
from selenium import webdriver
from page.register_page import RegisterPage
from common.connnect_mysql import DbConnect, dbinfo
from page.user_login_page import UserLoginPage
from page.user_feedbackiframe_page import FeedbackPage
from page.user_info_page import UserInfoPage


@pytest.fixture(scope='session', name='driver')
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    # driver.quit()


@pytest.fixture(scope='session')
def base_url():
    url = 'http://49.235.92.12:8200'
    return url


# 每个用例都要实例化，写在公共配置里
@pytest.fixture(scope='session')
def registerPage(driver, base_url):
    register = RegisterPage(driver, base_url)
    return register


@pytest.fixture(scope='session')
def db():
    _db = DbConnect(dbinfo, 'online')
    yield _db
    _db.close()


@pytest.fixture(scope='session')
def userLoginPage(driver, base_url):
    userlogin = UserLoginPage(driver, base_url)
    return userlogin


@pytest.fixture(scope='session')
def userFeedbackPage(driver, base_url):
    feedback = FeedbackPage(driver, base_url)
    return feedback


@pytest.fixture(scope='session')
def login_driver(driver, userLoginPage: UserLoginPage):
    """用户先登录，返回driver"""
    userLoginPage.open('/users/login/')
    userLoginPage.input_username('1234@qq.com')
    userLoginPage.input_password('123456')
    userLoginPage.click_login_btn()
    return driver


@pytest.fixture(scope='session')
def userInfoPage(login_driver, base_url):
    userinfo = UserInfoPage(login_driver, base_url)
    return userinfo