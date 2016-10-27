#coding=utf-8
__author__ = 'Administrator'

from TestBase.TestCaseBase import BaseTestCase
from TestPage.LoginPage import LoginPage
from TestBase.LoadXmlData import *


class LoginTest(BaseTestCase,LoginPage):

    def test_001(self):
        self.userlogin(self.driver,KEFU_USERNAME,KEFU_PASSWORD)
        self.assertTrue(self.driver.page_source.index(u'您好'))