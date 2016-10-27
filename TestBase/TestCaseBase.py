#coding=utf-8
__author__ = 'Administrator'

import unittest,time
from selenium import webdriver
from LoadXmlData import *


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(TESTURL)
        self.driver.implicitly_wait(30)
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()

