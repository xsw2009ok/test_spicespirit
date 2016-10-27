#coding=utf-8
__author__ = 'Administrator'

from TestBase.TestUtils import  Utils
from TestBase.LoginElement import *

class LoginPage(Utils):


    def userlogin(self,driver,user,passwd):
        self.wait()
        driver.find_element_by_xpath(LOGIN_CUSTOMER).click()
        self.wait(2)
        driver.find_element_by_id(LOGIN_USERNAME).send_keys(user)
        driver.find_element_by_id(LOGIN_PASSWORD).send_keys(passwd)
        driver.find_element_by_id(LOGIN_BUTTON_LOGIN).click()
        self.wait()


if __name__ == '__main__':
    l = LoginPage()
    l.userlogin()