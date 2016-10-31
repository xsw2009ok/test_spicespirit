#coding:utf-8
__author__ = 'Administrator'

from TestBase.OrderElement import *
from TestBase.TestUtils import *

class OrderPage():


    def loginInit(self,driver):
        driver.find_element_by_id(ORDER_MAINPAGE_CUSTOMER)